# FICO score column → "fico_score"
# Default column → "default"

#--------------Quantization Function--------

import pandas as pd
import numpy as np

def create_rating_buckets(df, n_buckets):

    fico = df['fico_score'].values
    default = df['default'].values

    # Sort by FICO
    sorted_data = sorted(zip(fico, default))
    fico_sorted = np.array([x[0] for x in sorted_data])
    default_sorted = np.array([x[1] for x in sorted_data])

    N = len(fico_sorted)

    # DP tables
    dp = np.full((N, n_buckets), -np.inf)
    split = np.zeros((N, n_buckets))

    def log_likelihood(start, end):
        segment = default_sorted[start:end+1]
        n = len(segment)
        k = np.sum(segment)

        if k == 0 or k == n:
            return 0

        p = k / n
        return k*np.log(p) + (n-k)*np.log(1-p)

    # Base case
    for i in range(N):
        dp[i][0] = log_likelihood(0, i)

    # DP recursion
    for b in range(1, n_buckets):
        for i in range(b, N):
            for j in range(b-1, i):
                val = dp[j][b-1] + log_likelihood(j+1, i)
                if val > dp[i][b]:
                    dp[i][b] = val
                    split[i][b] = j

    # Recover boundaries
    boundaries = []
    idx = N-1
    for b in range(n_buckets-1, 0, -1):
        idx = int(split[idx][b])
        boundaries.append(fico_sorted[idx])

    boundaries.sort()

    return boundaries



# Converting to Rating Map

def fico_to_rating(fico, boundaries):

    rating = 1
    for b in boundaries:
        if fico < b:
            return rating
        rating += 1

    return rating

#------Example-------

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

boundaries = create_rating_buckets(df, n_buckets=5)

print("Optimal FICO Boundaries:", boundaries)

# Example borrower
fico_score = 720
rating = fico_to_rating(fico_score, boundaries)

print("Borrower Rating:", rating)



#------Output Example-------

Optimal FICO Boundaries: [580, 630, 690, 740]
Borrower Rating: 2




    

# Converting to Rating Map


def create_rating_buckets(df, n_buckets=5):
    """Create rating boundaries based on quantiles of FICO scores."""
    quantiles = [i / n_buckets for i in range(1, n_buckets)]
    boundaries = df['FICO'].quantile(quantiles).tolist()
    return sorted(boundaries)


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

Optimal FICO Boundaries: [580, 630, 690,740] # type: ignore
Borrower Rating: 2

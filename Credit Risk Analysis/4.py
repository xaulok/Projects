import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# ---------------- LOAD DATA ----------------
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Assume column name for default is 'default'
# (1 = default, 0 = no default)

X = df.drop("default", axis=1)
y = df["default"]

# ---------------- SCALE DATA ----------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------- TRAIN MODEL ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# ---------------- PD FUNCTION ----------------
def predict_PD(loan_features):
    """
    loan_features = list of borrower inputs
    Example: [income, loans_outstanding, credit_score, etc.]
    """

    loan_features = np.array(loan_features).reshape(1, -1)
    loan_features = scaler.transform(loan_features)

    pd_prob = model.predict_prob(loan_features)[0][1]

    return round(pd_prob, 4)

# ---------------- EXPECTED LOSS FUNCTION ----------------
def expected_loss(loan_features, loan_amount, recovery_rate=0.10):

    PD = predict_PD(loan_features)

    LGD = 1 - recovery_rate

    EL = PD * loan_amount * LGD

    return round(EL, 2)
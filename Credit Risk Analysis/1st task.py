import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import os

# Load Data
file_path = os.path.join(os.path.dirname(__file__), "Nat_Gas.csv")
df = pd.read_csv(file_path)

# Convert Dates column to datetime
df['Dates'] = pd.to_datetime(df['Dates'])

# Sort data (important for time series)
df = df.sort_values('Dates')

# Convert dates into numeric values (number of days since start)
df['Days'] = (df['Dates'] - df['Dates'].min()).dt.days

# Create model
model = LinearRegression()
model.fit(df['Days'].values.reshape(-1,1), df['Prices'])

# ---------- Prediction Function ----------
def predict_gas_price(input_date):

    # Convert input date to datetime
    try:
        input_date = pd.to_datetime(input_date)
    except:
        return "Invalid date format. Use YYYY-MM-DD"

    days = np.array([[(input_date - df['Dates'].min()).days]])

    # Predict price
    predicted_price = model.predict(days)

    return round(predicted_price[0][0], 2)

# ---------- User Input ----------
date_input = input("Enter date (YYYY-MM-DD): ")

price = predict_gas_price(date_input)

print(f"Estimated Gas Price on {date_input}: {price}")

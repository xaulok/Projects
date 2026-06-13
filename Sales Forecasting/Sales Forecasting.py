import pandas as pd

# Loading the dataset
df = pd.read_csv("store sales Data.csv")

# Displaying the first few rows of the dataset
df.head()

# Converting Date column to datetime format and sorting the data by date
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# checking for missing values
df.isnull().sum()

# Aggregating Daily Sales
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Setting Date as index
daily_sales.set_index('Date', inplace=True)

# Resampling the data to monthly frequency and summing the sales
monthly_sales = daily_sales.resample('ME').sum()

# Displaying the monthly sales
print(monthly_sales)

# Plotting the monthly sales
import matplotlib.pyplot as plt  
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales['Sales'])
plt.xlabel('Date')
plt.ylabel('Monthly Sales')
plt.title('Sales Forecasting')
plt.show()

# Splitting the data into training and testing sets
train = monthly_sales[:-12]  # Using all but the last 12 months for training
test = monthly_sales[-12:]   # Using the last 12 months for testing

# Importing the ARIMA model
from statsmodels.tsa.arima.model import ARIMA

# Fitting the ARIMA model
model = ARIMA(train['Sales'], order=(1, 1, 1))  # (p, d, q) parameters
model_fit = model.fit()

# Forecasting the next 12 months
forecast = model_fit.forecast(steps=12)

# Displaying the forecasted values
print(forecast)

# Plotting the actual vs forecasted sales
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Sales'], label='Train')
plt.plot(test.index, test['Sales'], label='Test')
plt.plot(forecast.index, forecast, label='Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting')
plt.legend()
plt.show()

# Evaluating the model using Mean Absolute Error (MAE)
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
mae = mean_absolute_error(test['Sales'], forecast)
print(f'Mean Absolute Error: {mae}')

# Evaluating the model using Root Mean Squared Error (RMSE)
rmse = root_mean_squared_error(test['Sales'], forecast, squared=False)
print(f'Root Mean Squared Error: {rmse}')

# Evaluating the model using Mean Absolute Percentage Error (MAPE)
mape = mean_absolute_error(test['Sales'], forecast) / test['Sales'].mean()
print(f'Mean Absolute Percentage Error: {mape}')



# Prophet Forecasting
from prophet import Prophet
# Preparing the data for Prophet
prophet_data = monthly_sales.reset_index().rename(columns={'Date': 'ds', 'Sales': 'y'})
# Fitting the Prophet model
prophet_model = Prophet()
prophet_model.fit(prophet_data)
# Forecasting the next 12 months
future = prophet_model.make_future_dataframe(periods=12, freq='M')
prophet_forecast = prophet_model.predict(future)
# Displaying the forecasted values
print(prophet_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))

# Plotting the actual vs forecasted sales
plt.figure(figsize=(10, 6))
plt.plot(prophet_data['ds'], prophet_data['y'], label='Actual')
plt.plot(prophet_forecast['ds'], prophet_forecast['yhat'], label='Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting with Prophet')
plt.legend()
plt.show() 


# LSTM Forecasting
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(
    daily_sales[['Sales']]
)

from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(scaled_data.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
X_train = []
y_train = []
for i in range(60, len(scaled_data)):
    X_train.append(scaled_data[i-60:i, 0])
    y_train.append(scaled_data[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
model.fit(X_train, y_train, batch_size=1, epochs=1)
test_data = scaled_data[len(scaled_data) - len(test) - 60:]
X_test = []
y_test = daily_sales['Sales'][-len(test):].values
for i in range(60, len(test_data)):
    X_test.append(test_data[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)


# Evaluating the LSTM model
lstm_mae = mean_absolute_error(y_test, predictions)
print(f'LSTM Mean Absolute Error: {lstm_mae}')
lstm_rmse = root_mean_squared_error(y_test, predictions, squared=False)
print(f'LSTM Root Mean Squared Error: {lstm_rmse}')
lstm_mape = mean_absolute_error(y_test, predictions) / np.mean(y_test)
print(f'LSTM Mean Absolute Percentage Error: {lstm_mape}')

# Plotting the actual vs LSTM forecasted sales
plt.figure(figsize=(10, 6))
plt.plot(test.index, y_test, label='Actual')
plt.plot(test.index, predictions, label='LSTM Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting with LSTM')
plt.legend()
plt.show()

# Comparing the performance of ARIMA, Prophet, and LSTM models
print(f'ARIMA MAE: {mae}')
print(f'ARIMA RMSE: {rmse}')
print(f'ARIMA MAPE: {mape}')
print(f'Prophet MAE: {mean_absolute_error(test["Sales"], prophet_forecast["yhat"][-12:])}')
print(f'Prophet RMSE: {root_mean_squared_error(test["Sales"], prophet_forecast["yhat"][-12:], squared=False)}')
print(f'Prophet MAPE: {mean_absolute_error(test["Sales"], prophet_forecast["yhat"][-12:]) / test["Sales"].mean()}')
print(f'LSTM MAE: {lstm_mae}')
print(f'LSTM RMSE: {lstm_rmse}')
print(f'LSTM MAPE: {lstm_mape}')
# Based on the evaluation metrics, we can compare the performance of the ARIMA, Prophet, and LSTM models and choose the best one for sales forecasting.

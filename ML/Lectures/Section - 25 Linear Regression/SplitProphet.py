import pandas as pd
import numpy as np
import plotly.graph_objects as go
from prophet import Prophet
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error

st.title('Stock Price Prediction using Prophet')

# Load the data
df = pd.read_csv("ML/Lectures/Section - 25 Linear Regression/download.csv")

# Prepare the data for Prophet
df['date'] = pd.to_datetime(df['date'])
df = df.rename(columns={'date': 'ds', 'price': 'y'})

# Split data into train (80%) and test (20%)
split_index = int(len(df) * 0.8)
df_train = df[:split_index]
df_test = df[split_index:]

# Initialize and fit the Prophet model
model = Prophet()
model.fit(df_train)

# Make future dataframe for predictions
future = model.make_future_dataframe(periods=len(df_test))
forecast = model.predict(future)

# Extract test predictions
forecast_test = forecast.iloc[-len(df_test):]

# Calculate accuracy metrics
mae = mean_absolute_error(df_test['y'], forecast_test['yhat'])
mse = mean_squared_error(df_test['y'], forecast_test['yhat'])
rmse = np.sqrt(mse)

# Calculate accuracy percentage
accuracy = 100 - np.mean(np.abs((df_test['y'] - forecast_test['yhat']) / df_test['y'])) * 100

st.write(f"Mean Absolute Error (MAE): {mae}")
st.write(f"Mean Squared Error (MSE): {mse}")
st.write(f"Root Mean Squared Error (RMSE): {rmse}")
st.write(f"Accuracy: {accuracy:.2f}%")

# Get the predicted stock price for 2026-02-16
target_date = "2026-02-16"
predicted_price = forecast[forecast['ds'] == target_date]['yhat'].values

if len(predicted_price) > 0:
    st.write(f"### Predicted Stock Price on {target_date}: {predicted_price[0]:.2f}")
else:
    st.write(f"### No prediction available for {target_date}")

# Plot the forecast using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted'))
fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Actual'))

fig.update_layout(title='Stock Price Prediction', xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(fig)

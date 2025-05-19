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
# Assuming the CSV has columns 'Date' and 'Price'
df['date'] = pd.to_datetime(df['date'])
df = df.rename(columns={'date': 'ds', 'price': 'y'})

# Initialize the Prophet model
model = Prophet()

# Fit the model
model.fit(df)

# Make a future dataframe for predictions
future = model.make_future_dataframe(periods=365 * 2)  # Predicting 2 years into the future

# Predict the future
forecast = model.predict(future)

# Calculate accuracy metrics
mae = mean_absolute_error(df['y'], forecast['yhat'][:len(df)])
mse = mean_squared_error(df['y'], forecast['yhat'][:len(df)])
rmse = np.sqrt(mse)

# Calculate accuracy percentage
accuracy = 100 - np.mean(np.abs((df['y'] - forecast['yhat'][:len(df)]) / df['y'])) * 100

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
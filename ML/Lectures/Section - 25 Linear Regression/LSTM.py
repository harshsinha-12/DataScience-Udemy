import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler

# Load and prepare the data
def prepare_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Rename columns for Prophet
    df = df.rename(columns={'date': 'ds', 'price': 'y'})
    return df

# Train the Prophet model
def train_prophet_model(df):
    model = Prophet()
    model.fit(df)
    return model

# Generate future dates and make predictions
def make_predictions(model, df, periods=365):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

# Calculate RMSE and MAE
def evaluate_model(actual, predicted):
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    mae = mean_absolute_error(actual, predicted)
    return rmse, mae

# Main execution
def main():
    file_path = 'ML/Lectures/Section - 25 Linear Regression/download.csv'  # Update your file path
    df = prepare_data(file_path)
    
    # Split data into train and test sets (80-20 split)
    train_size = int(len(df) * 0.8)
    train_df = df.iloc[:train_size]
    test_df = df.iloc[train_size:]
    
    # Train the model
    model = train_prophet_model(train_df)
    
    # Make predictions
    forecast = make_predictions(model, df, periods=len(test_df))
    
    # Evaluate the model
    y_test = test_df['y'].values
    y_pred = forecast['yhat'].iloc[train_size:].values
    rmse, mae = evaluate_model(y_test, y_pred)
    
    print(f'Test RMSE: {rmse:.2f}')
    print(f'Test MAE: {mae:.2f}')
    
    # Predict stock price for a future date (e.g., 2026-02-16)
    future_date = pd.DataFrame({'ds': [pd.to_datetime('2026-02-16')]})
    future_prediction = model.predict(future_date)
    predicted_price_2026 = future_prediction['yhat'].values[0]
    print(f'Predicted Stock Price for 2026-02-16: ₹{predicted_price_2026:.2f}')
    
    # Plot forecast
    plt.figure(figsize=(15, 6))
    plt.plot(df['ds'], df['y'], label='Actual Price')
    plt.plot(forecast['ds'], forecast['yhat'], label='Predicted Price')
    plt.title('Stock Price Prediction using Facebook Prophet')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

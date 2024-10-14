from taipy.gui import Gui, notify
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objs as go
from datetime import date
import pandas as pd

# Initialize variables
START = "2011-01-01"
stocks = ['^NYFANG', 'RELIANCE.NS', 'TATAMOTORS.NS', 'KPITTECH.NS', 'TATAPOWER.NS', 'TITAN.NS', 'BTC-USD']

custom_today = date.today()
custom_stocks = ''
selected_stock = stocks[0]
n_years = 1

# Function to load data
def load_data(ticker, custom_today):
    data = yf.download(ticker, START, custom_today.strftime("%Y-%m-%d"))
    data.reset_index(inplace=True)
    return data

# Function to prepare data and make prediction
def make_forecast(stock_to_use, custom_today, n_years):
    period = n_years * 365
    data = load_data(stock_to_use, custom_today)
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=int(period))
    forecast = m.predict(future)
    return data, forecast, m

# Initialize data
data, forecast, m = make_forecast(selected_stock, custom_today, n_years)
last_date = forecast['ds'].iloc[-1]
last_yhat_lower = forecast['yhat_lower'].iloc[-1]
last_yhat_upper = forecast['yhat_upper'].iloc[-1]

# Function to update forecast when inputs change
def update_forecast():
    global data, forecast, m, last_date, last_yhat_lower, last_yhat_upper
    period = n_years * 365
    stock_to_use = custom_stocks.strip() if custom_stocks.strip() != '' else selected_stock
    data, forecast, m = make_forecast(stock_to_use, custom_today, n_years)
    last_date = forecast['ds'].iloc[-1]
    last_yhat_lower = forecast['yhat_lower'].iloc[-1]
    last_yhat_upper = forecast['yhat_upper'].iloc[-1]

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close', line=dict(color='green')))
    fig.update_layout(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    return fig

# Plot forecast
def plot_forecast():
    fig1 = plot_plotly(m, forecast)
    return fig1

# GUI Layout as a string using Taipy syntax
page = """
# Stock Price Predictor

Select a custom 'today' date:
<|{custom_today}|date|on_change=update_forecast|>

Enter custom stock name (in format of Yahoo Finance like RELIANCE.NS or select from below select box):
<|{custom_stocks}|input|on_change=update_forecast|>

Select Stock:
<|{selected_stock}|selector|options=stocks|on_change=update_forecast|>

Years of prediction:
<|{n_years}|slider|min=1|max=5|on_change=update_forecast|>

## Raw Data
<|{plot_raw_data()}|chart|>

## Forecast Data
<|{plot_forecast()}|chart|>

Predicted Price Range for {last_date.date()}:
- Lower Estimate: {last_yhat_lower:.2f}
- Upper Estimate: {last_yhat_upper:.2f}
"""

# Create and run the GUI
Gui(page=page).run()
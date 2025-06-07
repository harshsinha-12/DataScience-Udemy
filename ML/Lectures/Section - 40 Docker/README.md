# Stock Price Prediction App

This is a machine learning-based Flask application that predicts stock price movements for the next trading day. It uses historical stock data to train a Random Forest classifier model and provides predictions for whether a stock's price will go up or down.

## Features

- Predict next day price movement for any publicly traded stock
- Train custom models for specific stocks
- Simple, user-friendly web interface
- Containerized with Docker for easy deployment

## Prerequisites

- Docker and Docker Compose installed on your system
- Internet connection (for fetching stock data)

## Quick Start

1. Clone or download this repository
2. Navigate to the project directory
3. Build and run the Docker container:

```bash
docker-compose up --build
```

4. Open your web browser and navigate to `http://localhost:5001`
5. Enter a stock ticker symbol (e.g., AAPL for Apple) and click "Predict"

## Training a Model

The application needs to train a model before it can make predictions. 

1. Enter a stock ticker symbol in the input field
2. Click the "Train New Model" button
3. Wait for the model to be trained (this may take a few seconds)
4. Once trained, you can click "Predict Next Day Movement" to get predictions

## Tech Stack

- Flask: Web application framework
- scikit-learn: Machine learning library for the prediction model
- yfinance: Yahoo Finance API wrapper for fetching stock data
- NumPy & Pandas: Data manipulation and analysis
- Bootstrap: Frontend styling
- Docker: Containerization

## Docker Commands

Run using a pre-built image:
```bash
docker run -p 5001:5001 harshsinha12/stock-predictor
```

## Disclaimer

This application is for educational purposes only and should not be used for financial decisions. Stock market investments involve risk, and past performance does not guarantee future results.

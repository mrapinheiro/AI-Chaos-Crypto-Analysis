# Crypto ARIMA Forecast & Chaotic Time Series

This repository demonstrates how to:
- Fetch cryptocurrency market data (specifically Bitcoin) using **yfinance**  
- Calculate a simplified **Average True Range (ATR)** for volatility measurement  
- Generate a **chaotic time series** using the logistic map equation  
- Fit an **ARIMA model** to forecast cryptocurrency prices  
- Produce a data-driven **Buy/Hold/Sell** trading signal  

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Implementation Details](#implementation-details)
- [Usage](#usage)
- [Dependencies](#dependencies)

---

## Overview

This project is primarily for **educational** and **demonstrational** purposes. It pulls daily Bitcoin prices (BTC-USD) from Yahoo Finance, then uses a combination of **time series forecasting** and **heuristic-based signals** to generate a trading suggestion.

**Key components** include:
1. **Data Retrieval**: Fetches Bitcoin historical data from Yahoo Finance
2. **Chaotic Time Series Generation**: Maps a logistic map sequence to real price ranges using the equation `x_{i+1} = r * x_i * (1 - x_i)`
3. **ATR (Volatility) Filter**: Calculates a simplified Average True Range to detect high volatility periods
4. **ARIMA Forecasting**: Uses `statsmodels` to predict future prices with an ARIMA(1,1,1) model
5. **Heuristic Trading Signals**: Combines volatility check, day-over-day price change (>1.5%), and ARIMA forecasts to output "Buy," "Sell," or "Hold"

> **Note**: This is *not* financial advice or a production-ready trading bot. It simply illustrates some fundamental concepts in quantitative finance and chaos theory.

---

## Features

- **Fetch Crypto Data**: Download historical Bitcoin data using `yfinance` from 2017 to present
- **Calculate Simplified ATR**: Identifies high-volatility periods using a threshold of 500.0
- **Generate Chaotic Prices**: Scales a logistic map sequence (with parameters r=3.9, x0=0.5) to approximate real-world price ranges
- **ARIMA Forecast**: Predicts the next 5 data points using an ARIMA(1,1,1) model
- **Trading Instruction**: Issues a trading signal based on:
  - ATR threshold check (high volatility = "Hold")
  - >1.5% day-over-day price change triggering directional signals
  - ARIMA forecast comparison with current price

---

## Implementation Details

The implementation follows these steps:
1. Download BTC-USD historical data from 2017 to the current date
2. Extract close prices for analysis
3. Generate chaotic data using the logistic map with control parameter r=3.9
4. Calculate ATR using high, low, and previous close prices
5. Fit an ARIMA(1,1,1) model to forecast the next 5 days
6. Analyze crypto price data to provide a trading instruction based on:
   - ATR threshold check (default: 500.0)
   - Price change percentage check (threshold: 1.5%)
   - ARIMA forecast direction comparison

---

## Usage

Run the script directly:

```python
python crypto_prediction.py
```

The output includes:
- Historical Bitcoin data (head of dataframe)
- Chaotic prices (last 5 data points)
- ARIMA forecast for the next 5 days
- Chaotic price and ARIMA forecast for tomorrow
- Trading instruction for tomorrow (Buy/Hold/Sell)

---

## Dependencies

- **yfinance**: For downloading market data
- **numpy**: For numerical computations
- **pandas**: For data manipulation
- **statsmodels**: For ARIMA modeling
- **datetime**: For date handling

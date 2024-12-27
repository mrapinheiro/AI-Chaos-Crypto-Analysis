# Crypto ARIMA Forecast & Chaotic Time Series

This repository demonstrates how to:
- Fetch cryptocurrency market data (e.g., Bitcoin) using **yfinance**  
- Calculate a simplified **Average True Range (ATR)**  
- Generate a **chaotic time series** using the logistic map  
- Fit an **ARIMA model** to forecast crypto prices  
- Produce a basic **Buy/Hold/Sell** trading signal  

## Table of Contents
- [Overview](#overview)
- [Features](#features)

---

## Overview

This project is primarily for **educational** and **demonstrational** purposes. It pulls daily crypto prices (e.g., BTC-USD) from Yahoo Finance, then uses a combination of **time series forecasting** and **heuristic-based signals** to generate a trading suggestion.

**Key components** include:
1. **Chaotic Time Series Generation**: Demonstrates how to map a logistic map sequence to real price ranges.  
2. **ATR (Volatility) Filter**: Simplified approach to detect high volatility periods.  
3. **ARIMA Forecasting**: Uses `statsmodels` to predict future prices.  
4. **Heuristic Trading Signals**: Combines volatility check, day-over-day price change, and ARIMA forecasts to output “Buy,” “Sell,” or “Hold.”

> **Note**: This is *not* financial advice or a production-ready trading bot. It simply illustrates some fundamental concepts in quantitative finance and chaos theory.

---

## Features

- **Fetch Crypto Data**: Download historical Bitcoin data using `yfinance`.
- **Calculate Simplified ATR**: Identifies high-volatility periods that might invalidate forecasts.
- **Generate Chaotic Prices**: Scales a logistic map sequence to approximate real-world price ranges.
- **ARIMA Forecast**: Predicts the next 5 data points in a univariate time series.
- **Trading Instruction**: Issues a naive trading signal based on heuristics.

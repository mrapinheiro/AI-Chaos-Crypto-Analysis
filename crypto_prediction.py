import yfinance as yf
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

# -------------------------------------------------------------------------
# 1. Data Retrieval (Crypto) - Example: BTC-USD
# -------------------------------------------------------------------------
today = datetime.today().strftime('%Y-%m-%d')

# Download historical data for Bitcoin
df = yf.download('BTC-USD', start='2017-01-01', end=today)

# Extract close prices as a NumPy array
crypto_prices = df['Close'].values

# -------------------------------------------------------------------------
# 2. Chaotic Data Generation
# -------------------------------------------------------------------------
def generate_chaos(x0, r, n):
    """
    Generate a logistic map sequence commonly used to illustrate chaotic behavior:
      x_{i+1} = r * x_i * (1 - x_i).
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x


def generate_crypto_prices(x0, r, n, actual_prices):
    """
    Maps the chaotic sequence into the range of actual crypto prices.
    """
    chaos_data = generate_chaos(x0, r, n)
    min_price = min(actual_prices)
    max_price = max(actual_prices)
    crypto_prices_scaled = min_price + (max_price - min_price) * chaos_data
    return crypto_prices_scaled


# -------------------------------------------------------------------------
# 3. Average True Range (ATR) Calculation (Simplified)
# -------------------------------------------------------------------------
def calculate_atr(crypto_prices, window=14):
    """
    Simplified Average True Range (ATR) calculation.
    Uses:
      - High - Low
      - Absolute(High - previous Close)
    For a more standard approach, consider a rolling calculation.
    """
    high_prices = df['High'].values
    low_prices = df['Low'].values

    # Roll 'Close' by 1 day to get previous close
    prev_close = np.roll(crypto_prices, 1)

    # True Range
    tr = np.maximum(high_prices - low_prices, np.abs(high_prices - prev_close))
    # Simplified: take the mean over the first 'window' points
    atr = np.mean(tr[:window])
    return atr


# -------------------------------------------------------------------------
# 4. ARIMA Forecasting
# -------------------------------------------------------------------------
def forecast_crypto_prices(crypto_prices, order=(1, 1, 1)):
    """
    Fit an ARIMA model of the given order on the crypto price series.
    Forecast the next 5 steps.
    """
    model = ARIMA(crypto_prices, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)  # Forecast next 5 days
    return forecast


# -------------------------------------------------------------------------
# 5. Trading Instructions
# -------------------------------------------------------------------------
def analyze_crypto(crypto_prices, forecast, atr_threshold):
    """
    Heuristic to generate Buy/Hold/Sell signals for crypto based on:
      - ATR threshold (volatility filter)
      - Large day-over-day change (punctuated equilibrium)
      - ARIMA forecast comparison (if no big jump)
    """
    current_price = crypto_prices[-1]
    future_prices = forecast

    # Calculate ATR for the crypto
    atr = calculate_atr(crypto_prices)

    # 5.1 Volatility Check
    if atr > atr_threshold:
        return 'Hold'  # If volatility is too high, stay neutral

    # 5.2 Big Day-Over-Day Price Change
    previous_close = crypto_prices[-2]
    price_change_percent = (current_price - previous_close) / previous_close * 100

    if abs(price_change_percent) >= 1.5:
        if price_change_percent > 0:
            return 'Buy'
        else:
            return 'Sell'

    # 5.3 ARIMA Forecast Check
    future_avg_price = np.mean(future_prices)
    if future_avg_price > current_price:
        return 'Buy'
    elif future_avg_price < current_price:
        return 'Sell'
    else:
        return 'Hold'


# -------------------------------------------------------------------------
# 6. Putting It All Together
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Parameters for chaos and length
    x0 = 0.5          # Initial condition for logistic map
    r = 3.9           # Control parameter
    n = len(crypto_prices) + 1  # Number of data points to generate

    # Generate chaotic crypto-like data
    chaotic_prices = generate_crypto_prices(x0, r, n, crypto_prices)

    # Perform ARIMA forecasting
    forecast = forecast_crypto_prices(crypto_prices, order=(1, 1, 1))

    # Example ATR threshold (tweak based on typical BTC volatility)
    atr_threshold = 500.0

    # Analyze crypto for a trading decision
    trading_instruction = analyze_crypto(crypto_prices, forecast, atr_threshold)

    # Get today's and tomorrow's dates
    current_date = datetime.today().strftime('%Y-%m-%d')
    tomorrow_date = (datetime.today() + pd.DateOffset(days=1)).strftime('%Y-%m-%d')

    # Print results
    print('Historical Crypto Data (head):')
    print(df.head())

    print('\nChaotic Crypto Prices (last 5):')
    print(chaotic_prices[-5:])

    print('\nARIMA Forecast for Next 5 Days:')
    print(forecast)

    # Obtain tomorrow's “chaotic” price estimate & tomorrow’s forecast from ARIMA
    chaotic_price_tomorrow = chaotic_prices[-1]
    arima_forecast_tomorrow = forecast[0]

    print(f"\nChaotic Price for Tomorrow ({tomorrow_date}): {chaotic_price_tomorrow}")
    print(f"ARIMA Forecast for Tomorrow ({tomorrow_date}): {arima_forecast_tomorrow}")

    # Print trading instruction
    print(f"\n{tomorrow_date} - Trading Instruction: {trading_instruction}")
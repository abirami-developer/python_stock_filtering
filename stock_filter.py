
import yfinance as yf
import pandas as pd

# Define stock symbols (you can add more)
stock_list = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA"]

# Define filtering criteria
PRICE_THRESHOLD = 3000   # Max stock price
PE_RATIO_THRESHOLD = 30  # Max P/E Ratio
MARKET_CAP_THRESHOLD = 500e9  # Min Market Cap ($500B)

def fetch_stock_data(symbol):
    """Fetch stock data from Yahoo Finance."""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            "Symbol": symbol,
            "Price": info.get("currentPrice", None),
            "P/E Ratio": info.get("trailingPE", None),
            "Market Cap": info.get("marketCap", None),
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Fetch data for all stocks
stock_data = [fetch_stock_data(symbol) for symbol in stock_list]
stock_data = [s for s in stock_data if s]  # Remove None values

# Convert to DataFrame
df = pd.DataFrame(stock_data)

# Apply filtering (ensure that missing values are excluded)
filtered_stocks = df.dropna(subset=["Price", "P/E Ratio", "Market Cap"])  # Drop rows with missing critical data
filtered_stocks = filtered_stocks[
    (filtered_stocks["Price"] < PRICE_THRESHOLD) &
    (filtered_stocks["P/E Ratio"] < PE_RATIO_THRESHOLD) &
    (filtered_stocks["Market Cap"] > MARKET_CAP_THRESHOLD)
]

# Display results
print("Filtered Stocks:")
print(filtered_stocks)

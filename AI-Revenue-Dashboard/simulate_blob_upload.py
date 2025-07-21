
import os
import pandas as pd
import yfinance as yf
from datetime import datetime

# Create a simulated "blob" directory
os.makedirs("blob_storage", exist_ok=True)

# List of stocks (sample from S&P 500)
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Download recent data
data = {}
for ticker in tickers:
    df = yf.download(ticker, period="7d", interval="1d")
    df.to_csv(f"blob_storage/{ticker}_{datetime.now().strftime('%Y%m%d')}.csv")
    print(f"Saved {ticker} data to blob_storage/")

print("✅ Simulated Blob Upload complete.")

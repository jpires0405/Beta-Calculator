
import yfinance as yf
import pandas as pd

def download_prices(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    if isinstance(data, pd.Series):
        data = data.to_frame()
    return data.dropna()

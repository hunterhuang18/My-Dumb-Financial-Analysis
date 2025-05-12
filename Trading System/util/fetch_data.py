import yfinance as yf
import pandas as pd
import numpy as np
import os

def fetch_data(tickers, start_date, end_date = None, save_path = 'C:\\Users\\xizhenh\\Desktop\\Hunter\\Trading System\\data\\raw_data.csv'):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start = start_date, end = end_date)
        data[ticker] = df
    combined = pd.concat(data.values())
    combined.to_csv(save_path)
    print(f"Saved data to {save_path}")
    
if __name__ == "__main__":
    tickers = ['SPY', 'QQQ']
    start_date = '2024-5-12'
    fetch_data(tickers, start_date )
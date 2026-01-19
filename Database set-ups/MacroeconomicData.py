import yfinance as yf
import sqlite3
from datetime import date
import time

stock_database = sqlite3.connect("Database set-ups/StockData.db")
cursor = stock_database.cursor()

indexes = {"S&P 500": "^GSPC", "NASDAQ":"^IXIC"}

for INDEX in indexes.items():
    ticker = yf.Ticker(INDEX[1])

    stock_historical_data = ticker.history(start="2025-09-05", end="2026-01-19", interval="1d")
    for dat, row in stock_historical_data.iterrows():
        date_stamp = date.isoformat(dat)
        cursor.execute("""INSERT OR REPLACE INTO Indexes (IndexName, Date, Open, High, Low, Close, Volume)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?)
                          """, (INDEX[0], date_stamp, row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))
        stock_database.commit()
    
    time.sleep(2)

indicators = {"VIX": "^VIX",
              "13-Week Treasury":"^IRX",
              "5-Year Treasury":"^FVX",
              "Oil": "CL=F",
              "Gold ETF": "GLD"}

for INDICATOR in indicators.items():
    ticker = yf.Ticker(INDICATOR[1])

    stock_historical_data = ticker.history(start="2025-09-05", end="2026-01-19", interval="1d")
    for dat, row in stock_historical_data.iterrows():
        date_stamp = date.isoformat(dat)
        cursor.execute("""INSERT OR REPLACE INTO MarketIndicators (Indicator, Date, Open, High, Low, Close, Volume)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?)
                          """, (INDICATOR[0], date_stamp, row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))
        stock_database.commit()
    
    time.sleep(2)

currencies = {"EUR/USD":"EURUSD=X",
              "JPY/USD": "JPY=X",
              "GBP/USD":"GBPUSD=X",
              "USD/CHF":"CHF=X",
              "AUD/USD":"AUDUSD=X",
              "USD/CAD":"CAD=X",
              "NZD/USD":"NZDUSD=X"
              }

for CURRENCY in currencies.items():
    ticker = yf.Ticker(CURRENCY[1])

    stock_historical_data = ticker.history(start="2025-09-05", end="2026-01-19", interval="1d")
    for dat, row in stock_historical_data.iterrows():
        date_stamp = date.isoformat(dat)
        cursor.execute("""INSERT OR REPLACE INTO CurrencyExchange (Currencies, Date, Open, High, Low, Close, Volume)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?)
                          """, (CURRENCY[0], date_stamp, row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))
        stock_database.commit()
    
    time.sleep(2)
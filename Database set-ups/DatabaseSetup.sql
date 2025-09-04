-- Daily data of stock moves -- 
CREATE TABLE IF NOT EXISTS StockData (
    Ticker TEXT,
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Volume FLOAT,
    Dividends FLOAT,
    StockSplits FLOAT,
    PRIMARY KEY (Ticker, Date)
);

-- For tracking tickers for all of IT companies --
CREATE TABLE IF NOT EXISTS Tickers (
    CompanyName TEXT,
    Ticker TEXT
);

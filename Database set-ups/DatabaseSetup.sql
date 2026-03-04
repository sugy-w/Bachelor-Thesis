/* 
Table StockData stores the historical stock data for 65 IT companies
*/
CREATE TABLE IF NOT EXISTS StockData (
    "Ticker" TEXT,
    "Date" DATE,
    "Open" FLOAT,
    "High" FLOAT,
    "Low" FLOAT,
    "Close" FLOAT,
    "Volume" FLOAT,
    "Dividends" FLOAT,
    "StockSplits" FLOAT,
    PRIMARY KEY ("Ticker", "Date")
);

/*
Tables Indexes stores the historical data for NASDAQ + S&P 500
*/
CREATE TABLE IF NOT EXISTS Indexes (
    "IndexName" TEXT,
    "Date" DATE,
    "Open" FLOAT,
    "High" FLOAT,
    "Low" FLOAT,
    "Close" FLOAT,
    "Volume" FLOAT,
    PRIMARY KEY ("IndexName", "Date")
);

/*
Table MarketIndicators stores the historical data for VIX, Gold, Oil + Treausury Bonds (various maturities)
*/
CREATE TABLE IF NOT EXISTS MarketIndicators (
    "Indicator" TEXT,
    "Date" DATE,
    "Open" FLOAT,
    "High" FLOAT,
    "Low" Float,
    "Close" FLOAT,
    "Volume" FLOAT,
    PRIMARY KEY ("Indicator", "Date")
);

/*
Table CurrencyExchange stores the historical data for 7 major currency pairs (all include USD)
*/
CREATE TABLE IF NOT EXISTS CurrencyExchange (
    "Currencies" TEXT,
    "Date" DATE,
    "Open" FLOAT,
    "High" FLOAT,
    "Low" Float,
    "Close" FLOAT,
    "Volume" FLOAT,
    PRIMARY KEY ("Currencies", "Date")
);

/*
Table Tickers stores the mapping between company names and their corresponding stock tickers
*/
CREATE TABLE IF NOT EXISTS Tickers (
    "CompanyName" TEXT,
    "Ticker" TEXT
);

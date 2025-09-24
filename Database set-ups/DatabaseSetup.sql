/* DONE */
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

/* DONE */
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

/* DONE */
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

/* DONE */
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

CREATE TABLE IF NOT EXISTS Tickers (
    "CompanyName" TEXT,
    "Ticker" TEXT
);

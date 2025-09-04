import yfinance as yf
import sqlite3
from datetime import date
import time

'''
Dictionary holds all 68 companies listed in S&P 500 Stock Index with the GICS Sector "Information Technology"
GICS -> Global Industry Classification Standard, industry taxonomy developed for the purposes of S&P 
'''
tickers = tickers_reversed = {
    "ACN": "Accenture",
    "ADBE": "Adobe Inc.",
    "AMD": "Advanced Micro Devices",
    "AKAM": "Akamai Technologies",
    "APH": "Amphenol",
    "ADI": "Analog Devices",
    "AAPL": "Apple Inc.",
    "AMAT": "Applied Materials",
    "ANET": "Arista Networks",
    "ADSK": "Autodesk",
    "AVGO": "Broadcom",
    "CDNS": "Cadence Design Systems",
    "CDW": "CDW Corporation",
    "CSCO": "Cisco",
    "CTSH": "Cognizant",
    "GLW": "Corning Inc.",
    "CRWD": "CrowdStrike",
    "DDOG": "Datadog",
    "DELL": "Dell Technologies",
    "ENPH": "Enphase Energy",
    "EPAM": "EPAM Systems",
    "FFIV": "F5, Inc.",
    "FICO": "Fair Isaac",
    "FSLR": "First Solar",
    "FTNT": "Fortinet",
    "IT": "Gartner",
    "GEN": "Gen Digital",
    "GDDY": "GoDaddy",
    "HPE": "Hewlett Packard Enterprise",
    "HPQ": "HP Inc.",
    "IBM": "IBM",
    "INTC": "Intel",
    "INTU": "Intuit",
    "JBL": "Jabil",
    "KEYS": "Keysight Technologies",
    "KLAC": "KLA Corporation",
    "LRCX": "Lam Research",
    "MCHP": "Microchip Technology",
    "MU": "Micron Technology",
    "MSFT": "Microsoft",
    "MPWR": "Monolithic Power Systems",
    "MSI": "Motorola Solutions",
    "NTAP": "NetApp",
    "NVDA": "Nvidia",
    "NXPI": "NXP Semiconductors",
    "ON": "ON Semiconductor",
    "ORCL": "Oracle Corporation",
    "PLTR": "Palantir Technologies",
    "PANW": "Palo Alto Networks",
    "PTC": "PTC Inc.",
    "QCOM": "Qualcomm",
    "ROP": "Roper Technologies",
    "CRM": "Salesforce",
    "STX": "Seagate Technology",
    "NOW": "ServiceNow",
    "SWKS": "Skyworks Solutions",
    "SMCI": "Supermicro",
    "SNPS": "Synopsys",
    "TEL": "TE Connectivity",
    "TDY": "Teledyne Technologies",
    "TER": "Teradyne",
    "TXN": "Texas Instruments",
    "TRMB": "Trimble Inc.",
    "TYL": "Tyler Technologies",
    "VRSN": "Verisign",
    "WDC": "Western Digital",
    "WDAY": "Workday, Inc.",
    "ZBRA": "Zebra Technologies"
}


stock_database = sqlite3.connect("Database set-ups/StockData.db")
cursor = stock_database.cursor()

for TICKER in tickers.keys():
    ticker = yf.Ticker(TICKER)
    cursor.execute("INSERT INTO Tickers (CompanyName, Ticker) VALUES (?, ?)", (tickers[TICKER], TICKER))

    stock_historical_data = ticker.history(period="10y")
    for dat, row in stock_historical_data.iterrows():
        date_stamp = date.isoformat(dat)
        cursor.execute("""INSERT OR REPLACE INTO StockData (Ticker, Date, Open, High, Low, Close, Volume, Dividends, StockSplits)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (TICKER, date_stamp, row["Open"], row["High"], row["Low"], row["Close"], row["Volume"], row["Dividends"], row["Stock Splits"]))
        stock_database.commit()
    
    time.sleep(2)







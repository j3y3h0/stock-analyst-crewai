import yfinance as yf
import json

# ticker = "SPY"
ticker = "MSFT"
# ticker = "005930.KS" # 삼성전자
# ticker = "VOO"
# ticker = "IVV"
# ticker = "TSLA"
stock = yf.Ticker(ticker)

# history = history.to_csv()
print(f"history: {stock.history(period="3mo")}")
# print(f"info: {json.dumps(stock.info, indent=2)}\n")
print(f"news: {json.dumps(stock.news, indent=2)}\n")
print(f"income_stmt: {stock.income_stmt}\n")
print(f"balance_sheet: {stock.balance_sheet}\n")
print(f"insider_transactions: {stock.insider_transactions}\n")
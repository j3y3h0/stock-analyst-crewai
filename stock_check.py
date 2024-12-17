import yfinance as yf
import json

ticker = "SPY"
# ticker = "^GSPC"
# ticker = "MSFT"
# ticker = "005930.KS" # 삼성전자
# ticker = "VOO"
# ticker = "IVV"
# ticker = "TSLA"
stock = yf.Ticker(ticker)

info = "\n".join([f"{key}: {value}" for key, value in stock.info.items()])
# print(f"info: {info}")
# history = history.to_csv()
ret2 = list(map(lambda x: x["link"], stock.news))
# print(f"news: {ret2}")
print(f"history: {stock.history(period='6mo')}")
# print(f"info: {json.dumps(stock.info, indent=2)}\n")
# print(f"news: {json.dumps(stock.news, indent=2)}\n")
# print(f"income_stmt: {stock.income_stmt}\n")
# print(f"balance_sheet: {stock.balance_sheet}\n")
# print(f"insider_transactions: {stock.insider_transactions}\n")
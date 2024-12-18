import yfinance as yf
import json


ticker = "TSLA"
# ticker = "SPY"
# ticker = "^GSPC"
# ticker = "MSFT"
# ticker = "005930.KS" # 삼성전자
# ticker = "VOO"
# ticker = "IVV"


# 입력받은 name이 유효한 ticker인지 확인
try:
    stock = yf.Ticker(ticker)
    info = stock.info
    print(f"info: {json.dumps(stock.info, indent=2)}\n")
    
    # 'symbol'를 확인하여 유효성 검증
    if 'symbol' not in info or info['symbol'] is None:
        raise ValueError(f"'{ticker}'은(는) 유효한 티커가 아닙니다.")
    
except Exception as e:
    raise ValueError(f"'{ticker}'에 대해 티커 검증 중 오류가 발생했습니다: {e}")

info = "\n".join([f"{key}: {value}" for key, value in stock.info.items()])
print(f"info: {info}")
# history = history.to_csv()
ret2 = list(map(lambda x: x["link"], stock.news))
# print(f"news: {ret2}")
print(f"history: {stock.history(period='6mo')}")
# print(f"info: {json.dumps(stock.info, indent=2)}\n")
# print(f"news: {json.dumps(stock.news, indent=2)}\n")
# print(f"income_stmt: {stock.income_stmt}\n")
# print(f"balance_sheet: {stock.balance_sheet}\n")
# print(f"insider_transactions: {stock.insider_transactions}\n")
import os, sys
import asyncio
from dotenv import load_dotenv
from services.crew import StockAnalyst
from services.telegram import TelegramBot

# 실행 명령어 예시 
# ex)python main.py TSLA
# TSLA, AAPL, MSFT, NVDA
# XOM(엑손모빌), JNJ(존슨앤드존슨)
# SPY (S&P500)

load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_CHANNEL_ID1 = os.getenv('TG_CHANNEL_ID1')

if len(sys.argv) > 1:
    company = sys.argv[1]
else:
    company = None  # 기본값 설정 또는 에러 처리

if __name__ == "__main__":
    stock_analyst = StockAnalyst()
    result = stock_analyst.get_stock_analyst_result(company)

    telegram_bot = TelegramBot(token=TG_BOT_TOKEN, 
                               channel_id=TG_CHANNEL_ID1)
    # asyncio를 사용하여 비동기 함수 실행
    asyncio.run(telegram_bot.send_message(message=str(result)))

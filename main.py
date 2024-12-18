import os
import asyncio
from dotenv import load_dotenv
from services.crew import StockAnalyst, EtfAnalyst
from services.telegram import TelegramBot
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# ticker 예시 
# TSLA, AAPL, MSFT, NVDA
# XOM(엑손모빌), JNJ(존슨앤드존슨)
# SPY (S&P500)

load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_CHANNEL_ID1 = os.getenv('TG_CHANNEL_ID1')

if __name__ == "__main__":
    stock_analyst = StockAnalyst()
    etf_analyst = EtfAnalyst()

    telegram_bot = TelegramBot(token=TG_BOT_TOKEN, 
                               channel_id=TG_CHANNEL_ID1,
                               stock_analyst=stock_analyst,
                               etf_analyst=etf_analyst)
    
    def run_stock(company):
        result = stock_analyst.get_analyst_result(company)
        asyncio.run(telegram_bot.send_message(message=str(result))) # 비동기 실행
    
    def run_etf(company):
        result = etf_analyst.get_analyst_result(company)
        asyncio.run(telegram_bot.send_message(message=str(result)))

    # run_etf("SCHD")
    # run_stock("QUBT")

    # APScheduler 스케줄러 설정
    scheduler = BackgroundScheduler()
    
    # 0-6(월~일)
    scheduler.add_job(run_etf, CronTrigger(day_of_week="0", hour=21, minute=0), args=["SPY"]) # S&P500
    scheduler.add_job(run_stock, CronTrigger(day_of_week="1", hour=21, minute=0), args=["005930.KS"]) # 삼성전자
    scheduler.add_job(run_stock, CronTrigger(day_of_week="2", hour=21, minute=0), args=["NVDA"]) # 엔비디아
    scheduler.add_job(run_stock, CronTrigger(day_of_week="3", hour=21, minute=0), args=["MSFT"]) # 마이크로소프트
    scheduler.add_job(run_etf, CronTrigger(day_of_week="4", hour=21, minute=0), args=["SPY"]) # S&P500
    scheduler.add_job(run_stock, CronTrigger(day_of_week="5", hour=21, minute=0), args=["TSLA"]) # 테슬라
    scheduler.add_job(run_stock, CronTrigger(day_of_week="6", hour=21, minute=0), args=["AAPL"]) # 애플
    scheduler.start() # 스케줄러 시작

    telegram_bot.run()

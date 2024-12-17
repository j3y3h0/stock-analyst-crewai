import os, sys
import asyncio
import time
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

# if len(sys.argv) > 1:
#     company = sys.argv[1]
# else:
#     company = None  # 기본값 설정 또는 에러 처리

if __name__ == "__main__":
    stock_analyst = StockAnalyst()
    etf_analyst = EtfAnalyst()

    telegram_bot = TelegramBot(token=TG_BOT_TOKEN, 
                               channel_id=TG_CHANNEL_ID1)
    
    def run_stock(company):
        result = stock_analyst.get_analyst_result(company)
        asyncio.run(telegram_bot.send_message(message=str(result))) # 비동기 실행
    
    def run_etf(company):
        result = etf_analyst.get_analyst_result(company)
        asyncio.run(telegram_bot.send_message(message=str(result)))

    # run_etf("SPY")
    run_stock("005930.KS")

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

    print("스케줄러가 실행 중입니다. 예약된 작업이 실행되기를 기다립니다...")

    # 스케줄러 실행 상태를 유지하기 위해 무한 대기
    try:
        while True:
            time.sleep(5)  # 5초마다 대기
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # 종료 시 스케줄러 정리
        print("스케줄러가 종료되었습니다.")
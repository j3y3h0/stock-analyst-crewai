import os
import json
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from services.crew import StockAnalyst, EtfAnalyst

class TelegramBot:
    """
    Telegram 메시지 전송을 관리하는 클래스.
    """
    def __init__(self, 
                 token, 
                 channel_id, 
                 stock_analyst: StockAnalyst, 
                 etf_analyst: EtfAnalyst):
        """
        TelegramBot 객체 초기화
        :param token: Telegram 봇 토큰
        :param channel_id: 메시지를 보낼 채널 ID
        """
        self.bot = telegram.Bot(token=token)
        self.channel_id = channel_id
        self.user_ids = [user_id.strip() for user_id in os.getenv("USER_ID", "").split(",") if user_id.strip()]
        self.stock_analyst = stock_analyst
        self.etf_analyst = etf_analyst

    async def send_message(self, message):
        """
        지정된 채널에 메시지를 전송합니다.
        :param message: 전송할 메시지 내용
        """
        try:
            await self.bot.send_message(chat_id=self.channel_id, text=message)
        except Exception as e:
            print(f"Error while sending message: {e}")

    async def handle_command_stock(self, 
                                   update: Update, 
                                   context: ContextTypes.DEFAULT_TYPE):
        """
        /stock 명령어를 처리하는 핸들러
        """
        user_id = str(update.effective_user.id)
        
        # Private chat인지 확인
        if update.message.chat.type != "private":
            return

        # 권한 확인
        if user_id not in self.user_ids:
            return
        
        # 명령어 확인 및 파싱
        if len(context.args) != 1:
            await update.message.reply_text("사용법: /stock <티커>")
            return
        
        ticker = context.args[0]
        message = self.stock_analyst.get_analyst_result(ticker)
        
        # 결과 전송
        await update.message.reply_text(message)
        await self.bot.send_message(chat_id=self.channel_id, text=message)

    async def handle_command_etf(self, 
                                   update: Update, 
                                   context: ContextTypes.DEFAULT_TYPE):
        """
        /etf 명령어를 처리하는 핸들러
        """
        user_id = str(update.effective_user.id)
        
        # Private chat인지 확인
        if update.message.chat.type != "private":
            return

        # 권한 확인
        if user_id not in self.user_ids:
            return
        
        # 명령어 확인 및 파싱
        if len(context.args) != 1:
            await update.message.reply_text("사용법: /etf <티커>")
            return
        
        ticker = context.args[0]
        message = self.etf_analyst.get_analyst_result(ticker)
        
        # 결과 전송
        await update.message.reply_text(message)
        await self.bot.send_message(chat_id=self.channel_id, text=message)

    def run(self):
        """
        Telegram 봇 실행
        """
        application = ApplicationBuilder().token(self.bot.token).build()
        application.add_handler(CommandHandler("stock", self.handle_command_stock))
        application.add_handler(CommandHandler("etf", self.handle_command_etf))
        
        print("bot is running...")
        application.run_polling()


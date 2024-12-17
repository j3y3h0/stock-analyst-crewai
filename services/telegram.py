import telegram

class TelegramBot:
    """
    Telegram 메시지 전송을 관리하는 클래스.
    """
    def __init__(self, token, channel_id):
        """
        TelegramBot 객체 초기화
        :param token: Telegram 봇 토큰
        :param channel_id: 메시지를 보낼 채널 ID
        """
        self.bot = telegram.Bot(token=token)
        self.channel_id = channel_id

    async def send_message(self, message):
        """
        지정된 채널에 메시지를 전송합니다.
        :param message: 전송할 메시지 내용
        """
        try:
            await self.bot.send_message(chat_id=self.channel_id, text=message)
            print(f"Message sent successfully: {message}")
        except Exception as e:
            print(f"Error while sending message: {e}")


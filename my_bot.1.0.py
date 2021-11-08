import os
import time
from dotenv import load_dotenv

from func_bot import Bot

load_dotenv()

token = os.getenv('telegram_token')
bot = Bot(token)

while True:
    message = bot.get_message()
    if message is not None:
        bot.send_message(message['chat_id'], message['text'])
    time.sleep(2)
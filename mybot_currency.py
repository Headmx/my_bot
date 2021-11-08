import telebot
from course_in_belarusbank import course
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('telegram_token2')
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('USD', 'EUR', 'RUB', 'конверсии', 'все курсы')

@bot.message_handler(commands=['start'])
def start_message(message):
    stiker_id = 'CAACAgIAAxkBAAEDPZlhiRM7Ruju_99OLfOw4-JovJaFYQACDwADWbv8JQfeqhosCZ80IgQ'
    bot.send_sticker(message.chat.id, stiker_id)
    bot.send_message(message.chat.id, 'Привет, я бот по курсам валют', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, course(message.text))
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет узнай курсы валют и беги в банк')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, надеюсь ты заработал')

bot.polling(none_stop=True)


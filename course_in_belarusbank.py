import requests
import os
from bs4 import BeautifulSoup

url = 'https://belarusbank.by/api/kursExchange/minsk'
response = requests.get(url).json()
def course(message):
    city = response[0]['name']
    city_v = response[0]['name_type']
    buy_usd = response[0]['USD_in']
    sell_usd = response[0]['USD_out']
    buy_eur = response[0]['EUR_in']
    sell_eur = response[0]['USD_out']
    buy_rus = response[0]['RUB_in']
    sell_rus = response[0]['RUB_out']
    usd_eur_buy = response[0]['USD_EUR_in']
    usd_eur_sell = response[0]['USD_EUR_out']
    if message.lower() == 'usd':
        result = f'Сегодня в Беларусбанке {city_v}{city} следующие курсы {message}\nUSD:\t{buy_usd}/ {sell_usd}'
        return result
    if message.lower() == 'eur':
        result = f'Сегодня в Беларусбанке {city_v}{city} следующие курсы {message}\nEUR:\t{buy_eur}/ {sell_eur}'
        return result
    if message.lower() == 'rub':
        result = f'Сегодня в Беларусбанке {city_v}{city} следующие курсы {message}\nRUB:\t{buy_rus}/ {sell_rus}'
        return result
    if message.lower() == 'конверсии':
        result = f'Сегодня в Беларусбанке {city_v}{city} следующие курсы {message}\n' \
                 f'конверсии покупка (USD/EUR) {usd_eur_buy}\n' \
                 f'конверсии продажа (USD/EUR) {usd_eur_sell}'
        return result
    if message.lower() == 'все курсы':
        result = f'Сегодня в Беларусбанке {city_v}{city} следующие курсы\nUSD:\t{buy_usd}/ {sell_usd}\nEUR:\t{buy_eur}/ {sell_eur}\n' \
                f'RUB:\t{buy_rus}/ {sell_rus}\n\n' \
                f'конверсии покупка (USD/EUR) {usd_eur_buy}\n' \
                f'конверсии продажа (USD/EUR) {usd_eur_sell}'
        return result
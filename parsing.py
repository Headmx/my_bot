
import requests
from bs4 import BeautifulSoup

url = 'https://www.nbrb.by/statistics/rates/currbasket'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
values = soup.find_all('b')
names = soup.find_all('span', class_='text')
for value in values:
    print (value.text)


import requests
from bs4 import BeautifulSoup

url = 'https://www.nbrb.by/statistics/rates/currbasket'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
names = soup.find_all('span', class_='text')
values = soup.find_all('b', class_='align-right')

print(values)



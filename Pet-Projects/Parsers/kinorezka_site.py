import requests
import fake_useragent
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

ua = fake_useragent.UserAgent()

headers = {'User-Agent': ua.random, "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}

url = 'https://kinorezka.site/anime/'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

country = soup.find('div', class_='short-item').find_all('li')[1].text
year = soup.find('div', class_='short-item').find('li').text
name = soup.find('div', class_='short-item').find('a', class_='short-title fx-1').text
link = soup.find('div', class_='short-cols fx-row').find('a', class_='short-title fx-1').get('href')


data = []

for p in range(1, 2):
    print(p)
    url = f'https://kinorezka.site/anime/page/{p}'
    r = requests.get(url, headers=headers)
    sleep(3)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.find_all('div', class_='short-item')


    for film in films:
        try:
            country = film.find_all('li')[1].text
        except:
            country = '-'
        try:
            year = film.find('li').text
        except:
            year = '-'
        try:
            name = film.find('a', class_='short-title fx-1').text
        except:
            name = '-'
        try:
            link = soup.find('div', class_='short-cols fx-row').find('a', class_='short-title fx-1').get('href')
        except:
            link = '-'
        data.append([name, year, country, link])
print(len(data))

header = ['name', 'year', 'country', 'link']
df = pd.DataFrame(data, columns=header)
df.to_csv('./anime.csv', sep=';', encoding='utf-8')

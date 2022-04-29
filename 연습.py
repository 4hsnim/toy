import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://weather.naver.com/today/09140104',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('#content > div > div.section_center > div.card.card_today > div.today_weather > div.weather_area > div.weather_quick_area > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > dl > dd')
print(title)
# 코딩 시작
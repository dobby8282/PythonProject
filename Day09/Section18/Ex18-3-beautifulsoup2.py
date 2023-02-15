'''
파일명 : Ex18-3-beautifulsoup2.py

'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
review_list = soup.find_all('div', class_='list_content')

news_in = []
for result in review_list:
    news_in.append(result.text.strip())

for rank in news_in:
    print(rank)

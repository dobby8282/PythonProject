'''
파일명 : Ex18-2-beautifulsoup.py

bs4


https://movie.naver.com/movie/bi/mi/basic.nhn?code=10016
'''

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 10016}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div', class_='score_reple')

for review in review_list:
    print(review.find('p').text.strip())









'''
파일명 : Ex18-5-getRankPage.py

라이브러리 > 패키지(모듈이 모여있는 폴더) > 모듈(파이썬파일(.py))

'''
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
result_list = soup.find_all('td', class_='title')
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip())

for person in movie_in:
    print(person)


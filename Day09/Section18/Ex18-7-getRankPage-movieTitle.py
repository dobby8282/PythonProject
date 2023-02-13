import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('tr')
up_list = []
for movie in movie_list:
    target_list = movie.find_all('td', class_='ac')
    if target_list:
        if target_list[1].find('img', class_='arrow').get('alt') == 'up':
            up_list.append(movie.find('td', class_='title').text.strip())

for up_movie in up_list:
    print(up_movie)
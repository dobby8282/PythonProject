'''
파일명 : Ex18-3-beautifulsoup2.py

'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
# param = {}
response = requests.get(url)
html = response.text
print(response.status_code)


# soup = BeautifulSoup(html, 'html.parser')
#
# review_list = soup.find_all('div', class_='score_reple')
#
# for review in review_list:
#     print(review.find('p').text.strip())

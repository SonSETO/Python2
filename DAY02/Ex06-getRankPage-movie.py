'''
파일명 : Ex06-getRankpage-movie.py
'''
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/boxoffice/weekly'
response = requests.get(url)
html = response.text

soup=BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('strong', class_='tit_item')

for idx, movie in enumerate(movie_list):
    print('{}위: {}'.format(idx+1, movie.text.strip()))
    #print(movie.text.strip())
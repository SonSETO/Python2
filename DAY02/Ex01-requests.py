'''
파일명 : Ex01-requests.py

requests 라이브러리
  HTTP 요청을 보내기 위한 간편하고 인기 있는 라이브러리
  이를 사용하면 웹 페이지를 가져오거나, API와 상호 작용할 수 있다.
  
'''

import requests


url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code' : 161967}
response = requests.get(url, params=param)
print(response.text)
# 웹 사이트의 정보를 가지고 오고 싶다.
import requests
from bs4 import BeautifulSoup
# 1. 정보가 있는 사이트 URL확인
url = 'https://finance.naver.com/sise/'

# 2. 요청 
#response = requests.get(url)
#print(response) 
# #responnse 200은 성공적으로 원하는 정보를 받았다.
# 404,400 등 에러 내가 잘모샇ㄴ거
# 500은 개발자 잘못 

response = requests.get(url).text
print(response,type(response)) 

# 2.1 BeautifulSoup (text -> 다른 객체)
#텍스트 데이터를 HTML구조로 변환(HTML 파일에 있는 정보를 가져오기 위해 )
data = BeautifulSoup(response, 'html.parser')
print(data,type(data))
#원하는 정보를 뽑아서 출력 
kospi = data.select_one('#KOSPI_now')
print(kospi.text)



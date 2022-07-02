import requests
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/marketindex'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result = exchange.text
exchange2 = data.select_one('#exchangeList > li.on > a.head.jpy > div > span.value')
result2 = exchange2.text


print('현재 원/달러 환율은 ' + result + '입니다.')
print('현재 원/엔화 환율은'+result2+'입니다.')
# print(f'현재 원/달러 환율을 {result}입니다.')


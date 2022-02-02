from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://news.daum.net/ranking/kkomkkom"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')  
rank = 1

# 결과 콘솔창에 프린트하기
print(datetime.today().strftime('%Y년 %m월 %d일의 열독률 높은 순의 다음 뉴스 순위입니다.'), '\n')

# parsing 및 결과 프린트
results = soup.find('ul', 'list_newsissue').findAll('a', 'link_txt')
for result in results:
    print(rank, "위: ", result.get_text().strip())
    rank += 1

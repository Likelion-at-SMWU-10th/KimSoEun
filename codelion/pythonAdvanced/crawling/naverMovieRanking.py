from bs4 import BeautifulSoup
import requests
from datetime import datetime

'''
BeautifulSoup의 단점
    js로 데이터가 내려지기 전의 html 소스를 다운받기 때문에 실시간으로 서버에서 받아오는 정보들은 확인할 수가 없다.
    따라서 동적 기능들이 모두 완료된 후의 html을 받고 싶다면 Selenium의 webdriver를 이용해야 한다.
실시간 검색어들은 거의 동적으로 값을 넣던디.. -> 네이버 영화 랭킹 크롤링으로 프로젝트 변경
'''

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
# 일반 브라우저처럼 요청하기 위한 헤더값 (몇몇 사이트들은 크롤러를 막고 있기 때문)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests.get(url, headers=headers)

'''
한글 인코딩 오류 날 때 해결하는 방법
1) response.encoding = 'utf-8' 로 설정한 후, response.text를 읽어온다.
2) response.content를 읽어온다.

response.text와 response.content의 차이
text) 문서의 인코딩 방식을 자동적으로 추측하고 그에 맞게 디코딩
content) HTTP Response의 body 부분이 bytes 상태로 그대로 저장
'''
# 방법 1
response.encoding = 'utf-8' # 'daum.net' 사이트에선 encoding = 'ISO-8859-1'로 되어 있어서 한글이 깨졌던 것.
soup = BeautifulSoup(response.text, 'html.parser')  

# 방법 2
soup = BeautifulSoup(response.content, 'html.parser')  

result_text = ""
rank = 1

result_text += datetime.today().strftime('%Y년 %m월 %d일의 네이버 영화 랭킹 순위입니다.') + '\n\n'

# parsing
results = soup.find('table', 'list_ranking').findAll('a')
for result in results:
    result_text += str(rank) + '위: '
    result_text += result.get_text().strip() + '\n'
    rank += 1

# 결과물 파일에 저장하기
file = open("movieRanking.txt", "w", encoding='utf-8')
file.write(result_text)
file.close()

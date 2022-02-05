import requests
import json

# API key 값 찾아오기 (.gitignore로 API key 숨겨둠)
f = open("key.txt", "r")
apikey = f.readline()
f.close()

# API 파라미터 설정
city = "Seoul"
lang = "kr"
units = "metric"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}" # 문자열 맨 앞에 f를 붙이면 중괄호를 사용하여 파이썬의 변수를 넣을 수 있음

# API 결과 값 받기
result = requests.get(api)
data = json.loads(result.text)  # json 모듈을 통해 딕셔너리 형태로 변환

#  추출
print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
print("현재 온도는", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는", data["main"]["feels_like"], "입니다.")
print("최저 기온은", data["main"]["temp_min"], "입니다.")
print("최고 기온은", data["main"]["temp_max"], "입니다.")
print("습도는", data["main"]["humidity"], "입니다.")
print("풍속은", data["wind"]["speed"], "입니다.")

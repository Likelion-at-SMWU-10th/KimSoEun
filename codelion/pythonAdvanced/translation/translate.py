from googletrans import Translator

# 참고: https://pypi.org/project/googletrans/
translator = Translator()   

sentence = input("언어를 감지할 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요? ")

# 언어 감지
detected = translator.detect(sentence)

# 번역
result = translator.translate(sentence, dest)

# 결과 출력
print("=====출력 결과=====")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("===================")
import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 465

# 이메일 주소 유효성 검사 함수
def sendEmail(addr):
    reg = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # "계정@도메인.최상위도메인" 정규표현식
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

# 계정 정보 가져오기 (.gitignore로 정보 숨겨둠)
accountFile = open("account.txt", "r")
fromEmail = accountFile.readline()
pw = accountFile.readline()
toEmail = accountFile.readline()
accountFile.close()
print(toEmail)

# 사진 정보 바이너리 형태로 가져오기
with open("circle.png", "rb") as image: # close() 없이 파일 읽기 (직접 안해줘도 되니까 안전)
    image_file = image.read()
image_type = imghdr.what('circle', image_file)  # 이미지 확장자 판단

# 메일 content 설정
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message.add_attachment(image_file, maintype='image', subtype='png') # 이미지 첨부

# 메일 header 설정
message["Subject"] = "이것은 제목입니다."
message["From"] = fromEmail
message["To"] = toEmail

# 메일 보내기
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(fromEmail, pw)
sendEmail(toEmail)
smtp.quit()

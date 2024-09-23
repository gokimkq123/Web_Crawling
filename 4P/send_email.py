import smtplib
from email.mime.text import MIMEText
from email.header import Header

# MIMEText 객체로 메일을 생성한다.
msg = MIMEText('메일 본문')

# 제목에 한글이 포함될 경우 Header 객체를 사용한다.
msg['Subject'] = Header('메일 제목', 'utf-8')
msg['From'] = 'me@example.com'
msg['To'] = 'you@example.com'

# SMTP의 첫 번쨰 매개변수에 SMTP 서버의 호스트 이름을 지정한다.
with smtplib.SMTP('localhost') as smtp:
    # 메시지 전송
    smtp.send_message(msg)
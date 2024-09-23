import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()

# set_url로 robots.txt URL을 설정한다.
rp.set_url('https://www.donga.ac.kr/robots.txt')

# read로 robots.txt를 읽어 들인다.
print(rp.read())

# can_fetch의 첫 번째 매개변수에는 User-Agent 문자열,
# 두 번째 매개변수에 URL을 지정하면 해당 URL을 크롤링해도 괜찮은지 알 수 있다.
print(rp.can_fetch('mybot', 'https://www.donga.ac.kr/'))
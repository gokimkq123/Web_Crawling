import sys
from urllib.request import urlopen

f = urlopen('https://hanbit.co.kr/')


# 인코딩 방식을 추출하고 디코딩하기
encoding = f.info().get_content_charset(failobj="utf-8")

print('encoding:', encoding, file = sys.stderr)  # sys.stderr은 에러 발생시 관련 내용을 출력하는 것이다.(오류 났을때 나타나는 빨간색)

# 추출한 인코딩 방식으로 디코딩 한다.
text = f.read().decode(encoding)

print(text)
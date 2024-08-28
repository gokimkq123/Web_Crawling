# meta 태그에서 인코딩 방식 추출하기

import re
import sys
from idlelib.iomenu import encoding
from urllib.request import urlopen

f = urlopen('https://hanbit.co.kr/store/books/full_book_list.html')

# bytes형으로 일단 변수에 저장한다.
bytes_content = f.read()

# meta 태그에 charset은 보통 앞에 많이있다.
# 본문의 앞부분인 1024바이트를 ASCII 문자로 디코딩 해준다.
scanned_txt = bytes_content[:1024].decode('ascii', errors = 'replace')

# 디코딩한 문자열에서 정규 포현식으로 charset 값을 추출한다.
match = re.search(r'charset = ["\']?([\w-]+)', scanned_txt)

if match:
    encoding = match.group(1)
else:
    # charset이 없으면 utf-8 사용
    encoding = 'utf-8'

print('encoding:', encoding, file=sys.stderr)
text = bytes_content.decode(encoding)
sys.stdout = open('dp.html', 'w')
print(text)
sys.stdout.close()





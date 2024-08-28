import re
from html import unescape

# dp.html파일 열고 변수에 저장
with open('dp.html') as f:
    html = f.read()
# print(html)
# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출
# findall은 [a-z]+과 매치되는 모든 값을 찾아 리스트로 리턴한다.
# re.DOTALL은 줄바꿈 문자에 상관없이 검색할 때 많이 사용한다.

for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # 도서의 URL 추출
    url = re.search(r'<a href="(.*?)">',partial_html).group(1)
    url = 'https://hanbit.co.kr/' + url

    # re.sub는 패턴을 원하는 값(나는 '')로 대체한다
    title = re.sub(r'<.*?>', '', partial_html)

    print('url: ', url)
    print('title: ', title)
    print('---')


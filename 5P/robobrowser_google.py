import re
from robobrowser import RoboBrowser

# RoboBrowser 객체를 생성한다.
# 키워드 매개변수 parser는 BeautifulSoup의 두 번째 매개변수와 같다.
browser = RoboBrowser(parser='html.parser')

# open 메서드로 구글 메인 페이지를 연다.
browser.open('https://www.google.co.kr/')

# 키워드를 입력한다.
form = browser.get_form(action='/search')
form['q'] = 'Python'
browser.submit_form(form, list(form.submit_fields.values())[0])

# 검색 결과 제목을 추출한다.
# select 메서드는 BeautifulSoup의 select 메서드와 같다.
for a in browser.select('h3 > a'):
    print(a.text)
    print(a.get('href'))
    print()
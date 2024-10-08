import time
import sys
import os

from pandas.io.clipboard import paste
from rdflib.parser import headers
from robobrowser import RoboBrowser

# 인증 정보를 환경변수에서 추출한다.
NAVER_ID = os.environ.get('NAVER_ID')
NAVER_PASSWORD = os.environ.get('NAVER_PASSWORD')

# RoboBrowser 객체를 생성한다.
'''
user-Agent란?
https://www.whatismybrowser.com/detect/what-is-my-user-agent/
크롤링이 안될땐 user-Agent를 이용해 직접 크롬에 접속하는 역할을 하는것이다.
'''

browser = RoboBrowser(
    # Beautiful Soup에서 사용할 파서를 지정한다.
    parser='html.parser',
    # 일반적인 웹 브라우저 User-Agent(FireFox)를 사용한다
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
)

def main():
    # 로그인 페이지를 연다.
    print('Acessing to sign in page....', file=sys.stderr)
    browser.open('https://nid.naver.com/nidlogin.login')

    # 로그인 페이지에 들어가졌는지 확인한다.
    assert '네이버 : 로그인' in browser.parsed.title.string

    # name='FrmNIDLogin'이라는 입력 양식을 채운다.
    form = browser.get_form(attrs={'name' : 'frmNIDLogin'})

    form['id'] = NAVER_ID
    form['pw'] = NAVER_PASSWORD

    # 입력 양식을 전송한다.
    # 로그인 때 로그인을 막는 것을 회피하고자 몇 가지 추가 정보 전송
    print('Signing in...', file=sys.stderr)
    browser.submit_form(form, headers={
        'Referer' : browser.url,
        'Accept-Language': 'ko,en-US;q=0.7,en;q=0.3',
    })

    # 주문 이력 페이지를 연다.
    browser.open('https://order.pay.naver.com/home?tabMenu=SHOPPING&frm=s_order')

    # 문제가 있을 경우 HTML 소스코드 확인
    # print(browser.parsed.prettify())

    # 주문 이력 페이지가 맞는지 확인
    assert '네이버페이' in browser.parsed.title.string

    # 주문 이력을 출력한다
    print_order_history()

def print_order_history():
    """
    주문 이력을 출력합니다.
    """
    # 주문 이력을 순회합니다: 클래스 이름은 개발자 도구로 확인합니다.
    for item in browser.select('.p_info'):
        # 주문 이력 저장 전용 dict입니다.
        order = {}
        # 주문 이력의 내용을 추출합니다.
        name_element = item.select_one('span')
        date_element = item.select_one('.date')
        price_element = item.select_one('em')
        # 내용이 있을 때만 저장합니다.
        if name_element and date_element and price_element:
            name = name_element.get_text().strip()
            date = date_element.get_text().strip()
            price = price_element.get_text().strip()
            order[name] = {
                'date': date,
                'price': price
            }
            print(order[name]['date'], '-', order[name]['price'] + '원')


if __name__ == '__main__':
    main()
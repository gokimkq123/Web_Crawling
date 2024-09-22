import requests
import lxml.html

def main():
    """
    세션을 사용하면 쿠키와 같은 상태 정보를 저장할 수 있고, 요청(Request)과 응답(Response) 사이에 연결 상태를 유지할 수 있다.
    이를 이용하면 사용자 인증이 필요한 웹 사이트에 접근할 수 있거나, 쿠키를 사용해서 접근 제한이 걸려 있거나, 상태 정보가 저장되어 있는 웹 사이트에 지속적인 접근이 가능하다.
    """

    session = requests.Session()

    # scrape_list_page() 함수를 호출해서 제너레이터를 추출한다.
    response = session.get('https://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')

        # yield 구문으로 제너레이터의 요소 반환
        yield url


if __name__ == '__main__':
    main()
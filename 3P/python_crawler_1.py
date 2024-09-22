import requests
import lxml.html

response = requests.get('https://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)

# 모든 링크를 절때 URL로 변환한다.
root.make_links_absolute(response.url)
for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)
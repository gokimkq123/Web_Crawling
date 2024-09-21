import lxml.html

# parse() 함수로 파일 경로를 지정할 수 있다.
tree = lxml.html.parse('dp.html')

# parse() 함수로 URL을 지정할수도 있지만 추출할 떄 미세한 설정을 할 수 없으므로 추천하지 않는다.
# tree = lxml.html.parse('https://gokimkq123.github.io/CV.github.io/')

# 파일 객체를 지정해서 파싱할 수도 있다.
from urllib.request import urlopen
tree = lxml.html.parse(urlopen('https://gokimkq123.github.io/CV.github.io/'))
print(type(tree))

html = tree.getroot() # getroot() 메서드로 html 루트 요소의 HtmlElemnet 객체를 추출할 수 있다.
print(type(html))


# fromstring() 함수로 문자열을 파싱할 수 있다.
html = lxml.html.fromstring('''
<html lang="en"><head>
    <meta charset="UTF-8">
    <title>CV</title>
</head>
<body>
    <nav class="nav">
        <a href="#" class="menu_nav">home</a>
        <a href="#CV" class="menu_nav">CV</a>
        <a href="#" class="menu_nav">Activity</a>
        <a href="#" class="menu_nav">Project</a>
    </nav>
</body></html>''')
print(type(html))
print(html.xpath('//a'))    # xpath() 메서드로 XPath와 일치하는 요소 목록을 추출할 수 있다.
print(html.cssselect('a'))  # cssselect() 메서드로 선택자와 일치하는 요소 목록을 추출할 수 있다.


# HTML 파일 일고ㅡ getroot() 메서드로 HtmlElement 객체 생성
tree = lxml.html.parse('dp.html')
html = tree.getroot()

# cssselect() 메서드로, a요소를 출력한다

for a in html.cssselect('a'):
    print(a.get('href'), a.text)
import feedparser

# parse 함수에 파일 경로, 파일 객체, xml 문자열 등을 지정한다.
d = feedparser.parse('it.rss')

# parse 함수에 URL을 지정하면 피드를 파싱할 수 있다.
d = feedparser.parse('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
print(d.version) # 피드이 버전을 추출한다.

# parse 함수의 반환값은 FeedParserDict 객체이다.
print(type(d))

# 피드의 타이틀을 추출한다.
print(d.feed.title)

# 딕셔너리 사용
print(d['feed']['title'])

# 피드 링크 추출
print(d.feed.link)

# 피드 설명 추출
print(d.feed.description)

# d.entries로 피들르 list 자료형으로 추출한다.
print(len(d.entries))

# 요소의 타이틀을 추출한다.
print(d.entries[0].title)


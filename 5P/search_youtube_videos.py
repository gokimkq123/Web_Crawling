import os
from apiclient.discovery import build

# 환경변수에서 API 키 추출하기
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

'''
YouTube API 클라이언트를 생성
build() 함수의 첫 번째 매개변수에는 API 이름
두 번째 매개변수에는 API 버전을 지정한다.
키워드 매개변수 developerKey에는 API 키를 지정한다.
'''

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

'''
키워드 매개변수로 매개변수를 지정하고
search.list 메서드를 호출한다.
list() 메서드를 실행하면 googleapiclient.http.HttpRequest가 반환 된다.
execute 메서드를 실행하면 실제 HTTP 요청이 보내지며, API 응답이 반환된다.
'''

search_response = youtube.search().list(
    part='snippet',
    q='요리',
    type='video'
).execute()

# search_response는 API 응답을 JSON으로 나타낸 dict 객체이다.
for item in search_response['items']:
    print(item['snippet']['title'])
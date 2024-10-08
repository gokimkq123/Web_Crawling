import requests
from cachecontrol import CacheControl

session = requests.session()
# session을 래핑한 cached_session 만들기
cached_session = CacheControl(session)

# 첫 번째는 캐시돼 있지 않으므로 서버에서 추출한 이후 캐시한다.
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)

# ETag와 Last-Modified 값을 사용해 업데이트됐는지 확인한다.
# 변경사항이 없는 경우에는 콘테츠를 캐시에서 추출해서 사용하므로 빠른 처리가 가능하다.
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)
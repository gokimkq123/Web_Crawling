import time
import requests

# 일시적인 오류를 나타내는 상태 코드를 지정한다.
TEMPORARY_ERROR_CODES = (408, 505, 502, 503, 504)

def main():
    response = fetch('https://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:   print('Success')
    else:   print('Error')


def fetch(url):
    """
    지정한 URL에 요청한 뒤 response 객체를 반환한다.
    일시적인 오류가 발생하면 최대 3번 재시도한다.
    """
    max_retries = 3
    retries = 0

    while True:
        try:
            print('Retrieving {0}...'.format(url))
            response = requests.get(url)
            print('Status: {0}'.format(response.status_code))
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response # 일시적이 오류가 아니라면 반환

        except requests.exceptions.RequestException as ex:
            # 네트워크 레벨 오류의 경우 재시도
            print('Exception: {0}'.format(ex))
            retries += 1
            if retries >= max_retries:
                # 재시도 횟수 상한을 넘으면 예외 발생
                raise Exception('Max retries exceeded')
            # 지수 함수적으로 재시도 간격을 증가시킨다.
            wait = 2 ** (retries - 1)
            print('Waiting {0} seconds...'.format(wait))
            time.sleep(wait)

if __name__ == '__main__':
    main()
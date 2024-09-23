import requests
from retrying import retry

# stop_max_attempt_number로 최대 재시도 횟수를 지정한다.
# wait_exponential_multiplier로 특정한 시간 만큼 대기하고 재시도하게 한다. 단위는 밀리초
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)

def main():
    response = fetch('https://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:   print('Success')
    else:   print('Error')

TEMPORARY_ERROR_CODES = (408, 505, 502, 503, 504)

def fetch(url):
    print('Retrieving {0}'.format(url))
    response = requests.get(url)
    print('Status code: {0}'.format(response.status_code))

    if response.status_code not in TEMPORARY_ERROR_CODES:
        return response

    raise Exception('Failed to fetch {0}'.format(response.status_code))

if __name__ == '__main__':
    main()
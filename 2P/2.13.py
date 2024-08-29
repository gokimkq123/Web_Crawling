import csv

# 유닉스는 줄바꿈 코드를 CRLF로 사용하기 떄문에 자동 변환 되지않게 newline=''을 쓴다
with open('2_13.csv', 'w', newline='', encoding='utf-8-sig') as f:
    # csv.writer는 파일 객체를 매개변수로 지정한다
    writer = csv.writer(f)
    # 첫 번째 줄에는 헤더를 작성한다
    writer.writerow(['rank', 'city', 'population'])
    # writerows에 리스트를 전달하면 여러 개의 값을 출력한다
    writer.writerows([
        [1, '상하이', 123],
        [2, '카라치', 124124],
        [3, '부산', 1231224],
        [4, '경남', 121113],
        [5, '서울', 1232344],

    ])

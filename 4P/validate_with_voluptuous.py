from voluptuous import Schema, Match

schema = Schema({    # 규칙 1 객체는 dict 자료형
    'name' : str,                 # 규칙 2 name은 str 자료형
    'price' : Match(r'^[0-9,]+$') # 규칙 3 price가 정규 표현식에 맞는지 확인
}, required=True) # 규칙 4 dict의 키는 필수

# Schema 객체는 함수처럼 호출해서 사용한다.
# 매개변수에 대상을 넣으면 유효성 검사를 수행한다.
schema({
    'name' : '포도',
    'price' : '3,000'
})

schema({
    'name' : None,
    'price' : '3,000',
}) # 유효성 검사 탈락

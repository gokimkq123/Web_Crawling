import MySQLdb

# MySQL 서버에 접속하고 연결을 변수에 저장한다.
# 사용자 이름과 비밀번호를 저장한 뒤 scraping 데이터베이스를 사용한다.
# 접속에 사용할 문자 코드는 utf8mb4로 지정한다.
conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

# 커서를 추출한다.
C = conn.cursor()

# execute() 메서드로 SQL 구문을 실행한다.
C.execute('DROP TABLE IF EXISTS cities')

#cities 테이블을 생성한다
C.execute('''
    CREATE TABLE cities(
        rank integer,
        citiy text,
        population integer
    )
''')


# execute 메서드의 두 번째 매개변수에는 파라미터를 지정할 수 있다
# SQL 내부에서 파라미터로 변경할 부분은 %s로 지정한다.
C.execute('INSERT INTO cities VALUES(%s, %s, %s)', (1, '상하이', 24150000))

# 파라미터가 딕셔너리일 때는 플레이스홀더를 %(<이름>)s 형태로 지정한다.
C.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
          {'rank' : 2, 'city' : '카라치', 'population' : 2350000})

# executemany 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서 실행 가능하다.
C.execute('INSERT INTO cities VALUES(%(rank)s, %(city)s, %(population)s)',
          [
              {'rank' : 3, 'city' : '베이징', 'population' : 12300},
              {'rank' : 4, 'city' : '텐진', 'population' : 12312400},
              {'rank' : 5, 'city' : '대한민국', 'population' : 11242300},
          ])

# 변경사항을 커밋한다.
conn.commit()

# 저장한 데이터를 추출한다.
C.execute('SELECT * FROM cities')

# 쿼리의 결과는 fetchall() 메서드로 추출한다.
for row in C.fetchall():
    print(row)

conn.close()

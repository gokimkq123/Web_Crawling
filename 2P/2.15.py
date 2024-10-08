import sqlite3

conn = sqlite3.connect('top_cities.db')

# 커서를 추출한다
c = conn.cursor()

# execute 메서드로 SQL 구문을 실행한다
# 스크립트를 여러 번 사용해도 같은 결과를 출력할 수 있게 cities 테이블이 존재하는 경우 제거한다
c.execute('DROP TABLE IF EXISTS cities')

#cities 테이블을 생성한다
c.execute('''
    CREATE TABLE cities(
        rank integer,
        citiy text,
        population integer
    )
''')

# execute 메서드의 두 번째 매개변수에는 파라미터를 지정할 수 있다
# SQL 내부에서 파라미터로 변경할 부분은 ?로 지정한다
c.execute('INSERT INTO cities VALUES (?,?,?)', (1, '상하이', 240000))

# 파라미터가 딕셔너리일 때는 플레이스홀더를 :<이름> 형태로 지정한다
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank' : 2, 'city' : '카라치', 'population' : 223340000})

# executemany 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서 여러 개의 SQL 구문을 실행 할 수 있다
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)',[
    {'rank' : 300, 'city' : '베이징', 'population' : 233340000},
    {'rank' : 4, 'city' : '부산', 'population' : 20000},
    {'rank' : 5, 'city' : '서울', 'population' : 340000},
])

# 변경사항을 커밋한다
conn.commit()

# 저장한 데이터를 주출한다
c.execute('SELECT * FROM cities')

#쿼리의 결과는 fetchall 메서드로 추출할 수 있다
for row in c.fetchall():
    print(row)


conn.close()
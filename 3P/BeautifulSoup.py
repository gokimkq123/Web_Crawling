from bs4 import BeautifulSoup

with open('dp.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# find_all 메서드로 a 요소를 추출하고 반복을 돌린다.
for a in soup.find_all('a'):
    print(a.get('href'), a.text)

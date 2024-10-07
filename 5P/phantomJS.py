from selenium import webdriver

# 웹 드라이버 생성
driver = webdriver.PhantomJS()

driver.implicitly_wait(3)

# 페이지 읽어 들이기
driver.get('https://www.naver.com/')

# 페이지 타이틀 확인하기
print(driver.title)

# 화면 크기 지정
driver.set_window_size(1920, 1080)
# 스크린샷 찍기
driver.save_screenshot('naver-1.png')
driver.quit()
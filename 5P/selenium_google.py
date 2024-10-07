from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Phantomjs 모듈의 WebDriver 객체를 생성한다.
driver = webdriver.PhantomJS()

# Google 메인 페인지를 연다.
driver.get('https://www.google.com/')

# 타이틀에 Google이 포함돼 있는지 확인한다.
assert 'Google' in driver.title

# 검색어를 입력하고 검색한다.
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# 타이틀에 Python이 포함돼 있는지 확인한다.
assert 'Python' in driver.title

# 스크린샷을 찍는다.
driver.save_screenshot('search_result.png')

# 검색 결과를 출력한다.
for a in driver.find_element_by_css_selector('a > h3'):
    print(a.text)
    # print(a.get_attribute('href'))
    print()
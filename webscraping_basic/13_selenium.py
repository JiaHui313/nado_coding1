# 웹 브라우저: 크롬, 사파리, 익스플로러...
import time
from selenium import webdriver # 셀리늄 심화과정(네이버로그인)

#크롬 웹드라이버 객체 생성하기
browser = webdriver.Chrome() #Chrome("chrome 드라이버 설치한 경로")
# 1. 네이버로 이동
browser.get("http://naver.com") #네이버로 이동

# 2.로그인버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4.로그인버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear() #naver_id 삭제후
browser.find_element_by_id("id").send_keys("my_id") #my_id 입력

# 6.html정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit() #전체 페이지 닫기
# browser.close() # 현재 탭 닫기


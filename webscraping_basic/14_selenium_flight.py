from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

#항공권 url로 이동하기
url = "http://flight.naver.com/flights"
browser.get(url) 

#가는 날, 오는 날 선택 click하기
browser.find_element_by_link_text("가는 날 선택").click()

#7월(이번달) 27-28일 선택
# browser.find_elements_link_text("27")[0].click() #[0]: 이번달 27일 선택
# browser.find_elements_link_text("28")[0].click() #[0]: 이번달 28일 선택

#8월(다음달 27-28일 선택)
# browser.find_elements_link_text("27")[1].click() #[1]: 다음달 27일 선택
# browser.find_elements_link_text("28")[1].click() #[1]: 다음달 28일 선택

#이번달 27일, 다음달 28일 선택
browser.find_elements_link_text("27")[0].click() #[0]: 이번달 27일 선택
browser.find_elements_link_text("28")[1].click() #[1]: 다음달 28일 선택

#여행장소(제주도) 정하기
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 브라우저 최대 10초간 대기, XPATH경로가 나올때까지
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div[2]/div[4]/ul/li[1]"))
    print(elem.text) #첫번째 가격 출력
finally:
    browser.quit()

#첫번째 가격 가져오기
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div[4]/ul/li[1]")
# print(elem.text)



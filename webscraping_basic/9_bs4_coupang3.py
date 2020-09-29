# BeautifulSoup4 활용 2-3 쿠팡페이지에서 광고가 붙은 itme은 제거하기
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    #광고제품은 제외
    ad_badge = item.find("span", attrs = {"class": "ad-badge-text"})
    if ad_badge:
        print("  <광고 상품 제외합니다.> ")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    
    #애플제품 제외
    if "Apple" in name:
        print(" <Apple 상품은 제외합니다.>")
        continue


    price =item.find("strong", attrs={"class": "price-value"}).get_text() #가격
    
    #리뷰 50개 이상, 평점 4.5이상 되는 것만 조회함
    rate =item.find("em", attrs={"class": "rating"})#평점
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품은 제외합니다.>")
        continue

    rate_count =item.find("span", attrs={"class": "rating-total-count"})#리뷰수
    if rate_count:
        rate_count = rate_count.get_text() #출력값 (26)
        rate_count = rate_count[1:-1]
        # print("리뷰수: ", rate_count)
    else:
        print("  <리뷰 없는 상품은 제외합니다.>")
        continue

    if float(rate) >= 4.5 and int(rate_count) >= 50:
        print(name, price, rate, rate_count)

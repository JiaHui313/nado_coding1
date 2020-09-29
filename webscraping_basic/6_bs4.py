import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup객체에서 처음 발견되는 a element를 반환
# print(soup.a.attrs) # a태그의 attrs(속성)들 가져오기
# print(soup.a["href"]) # a태그의 href속성인 '값'정보를 출력함

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))#class="Nbtn_upload"인 a element를 찾아줘.#find(a, )a: 찾아오고자 하는 정보/첫번째 element
# print(soup.find(attrs={"class": "Nbtn_upload"}))# class="Nbtn_upload"인 어떤 element를 찾아줘.

# print(soup.find("li", attrs ={"class": "rank01"}))
rank1 = soup.find("li", attrs ={"class": "rank01"})
print(rank1.a)
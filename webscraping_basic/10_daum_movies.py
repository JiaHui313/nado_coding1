# BeautifulSoup4 활용 3-1 다음웹페이지에서 영화순위 이미지들 다운받기

import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs = {"class": "thumb_img"})

for image in images:
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https://" + image_url #이미지 주소앞에 "https://"붙이기
    
    print(image_url)
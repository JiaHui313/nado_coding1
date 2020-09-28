# user agent """
# 3_requests에서 nadocidng.tistory.com에 접속하려고 했을 때 "403에러가 생김"
# 왜냐하면 웹사이트에서는 사용자의 정보(헤더정보)를 알수가 있음
# pc에서 접속(일반페이지) or 스마트폰접속(세로로 긴 페이지)에 따라 창화면의 크기가 다름

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)

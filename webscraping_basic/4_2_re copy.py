#정규식 기본2(re)
# 주민등록번호 901212-7845612 #옳바른 구조
#             abcdef-1111111 #틀린 구조

# 이메일주소
# nadocoding@gmail.com #옳바른 주소
# nudocoding@gamil@gmail.com #옳바르지 않은 주소

# IP주소 192.168.0.1 (O)    1000.2000.3000.4000(X)

import re #정규식 라이브러리 import
#예제) 차량번호판 4자리... abcd, book, desk...
#               ca?e: care, cafe, cave, ...
# caae, cabe, cace, cade, ....
p = re.compile("ca.e") # p: pattern 
#"원하는 형태" : 정규식
# ^(^de): 문자열의 시작 > desk, destination (o) | fade(매칭x)
# .(ca.a): 하나의 문자를 의미 > cafe, cafe, case(o) | caffe(매칭x)
# $(se$): 문자열의 끝을 의미 > case, base(o) | face(매칭x)

def print_match(m):
    if m:
        print("m.group(): ", m.group()) #group()은 일치하는 문자열을 반환
        print("m.string: ", m.string) #string은 입력받은 문자열을 그대로 출력
        print("m.start(): ", m.start()) #start()는 일치하는 문자열의 시작index
        print("m.end(): ", m.end())#end()는 일치하는 문자열의 끝index
        print("m.span(): ", m.span()) #sapn()은 일치하는 문자열의 시작, 끝index
    else:
        print("매칭되지 않았습니다.")

# m = p.match("care") #match(""):주어진 문자열의 처음부터 일치하는지 확인!
# print_match(m)
# print(m.group()) #매치되지 않으면 에러가 발생함

# m = p.search("good careless") #search():주어진 문자열 중에 일치하는게 있는지 확인함.
# print_match(m)

lst = p.findall("good care cafe") #findall():일치하는 모든 것을 리스트 형태로 반환
print(lst) #[care, cafe]

#1. p = re.compile("원하는 형태로")을 컴파일하고 
#2. m = p.match("비교할 문자열") :주어진 문자열의 처음부터 일치하는지 확인!
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인!
#4. lst = p.findall("비교할 문자열") : 일치하는 모든 것들을 "리스트"형태로 반환



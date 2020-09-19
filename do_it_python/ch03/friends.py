# 드라마 자막 가공
# friends.txt를 다운받아서 같은 폴더에 넣은 다음 프로그램을 실행합니다.

import os, re, codecs

#자신의 저장경로를 입력
os.chdir(r'C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\do_it_python\\ch03')
f = open('friends101.txt', 'r', encoding="utf-8")
script101 = f.read()

#문자열 객채 슬라이싱
print(script101[:100])

Line = re.findall(r'Monica:.+', script101)

#리스트 요소 중에서 앞에서 3개까지만 출력하기
print(Line[:3]) # 0, 1, 2 -> 3개

#모니카.txt 파일 만들기
f = open('monica.txt','w', encoding= "utf-8")
monica = ''
for i in Line:
    monica += i +'\n'
f.write(monica)
f.close() #파일 반드시 닫기

#모니카 대사만 출력하기
for item in Line[:3]:
    print(item)

#등장인물 이름 모으기
print(re.findall(r'[A-Z][a-z]+: ', script101))
print(set(re.findall(r'[A-Z][a-z]+: ', script101))) #이름 중복 지우기

#캐릭터 이름 한줄로 출력하기
character = [x[:-2] for x in list(set(re.findall(r'[A-Z][a-z]+: ', script101)))]
for i in character:
    print(i) #캐릭터 이름 각각 출력하기

#지문만 출력하기
re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101, re.VERBOSE) [:6]
f= open('friends101.txt', 'r')
sentences = f.readlines()
for i in sentences[:20]: #20개만 출력
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

# would가 나오는 문장만 출력하기
would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i ) and re.search('would',i)]
for i in would:
    print(i)

newf = open('would.txt', 'w')
newf.writelines(would)
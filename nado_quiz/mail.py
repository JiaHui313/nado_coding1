# 퀴즈) 당신은 (주)나도출판의 편집자입니다. 
# 최근에 파이썬에 관한 책을 기획 중인데 양질의 컨텐츠를 제공하는 유튜버들을 발견하여 제안서를 보내려고 합니다.
# 동일한 내용의 메일에 유튜버 이름 정보만 변경해서 파일로 저장하는 프로그램을 만드세요.

# 조건)
# 1. 유튜버 이름은 리스트로 제공( 최소 2명 이상)
# names = ["유튜버1", "유튜버2", ...]

# 2. 파일명은 '유튜버이름.txt'로 저장

# [메일본문]
# 안녕하세요? xxx님,
# (주)나도 출판 편집자 ..입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책을 출간 계획입니다.
# xxx님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서르 ㄹ확인 부탁드리며, 긍정적인 회신 기다리겠습니다.
# 감사합니다.
# -..드림

names = ["생활코딩", "나도코딩", "토르", "헐크에러"]

for name in names:
  with open("{}.txt".format(name), "w", encoding="utf-8") as email_file:
    contents = ( f"안녕하세요? {name}님,\n\n"
    "(주)나도 출판 편집자 ..입니다.\n"
    "현재 저희 출판사는 파이썬에 관한 주제로 책을 출간 계획입니다.\n"
    f"{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
    "자세한 내용은 첨부드리는 제안서르 ㄹ확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n"
    "감사합니다.\n\n"
    "-..드림")
    email_file.write(contents)

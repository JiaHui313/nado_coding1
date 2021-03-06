# 퀴즈) "사회적 거리두기"에 따른 영화관 좌석 예매 시스템을 만드세요.

# 각 열은 1 ~ 20 번까지 총 20개의 좌석으로 구성
# 예) a1, a2, a3, a4, ... a20
#     b1, b2, b3, b4, ... b20

# 이 때 a열에 대해서 홀수로 끝나는 좌석에 대해서만 출력
# (각 좌석은 " "(빈칸)로 구분)
# 예) a1 a3 a5 ... a19

# #풀이1
# for i in range(1, 20+1):
#     if i % 2 == 1: # i를 2로 나눈 나머지
#         print("a" + str(i), end=" ")

#풀이2 슬라이싱 이용하기
for i in range(1, 20+1)[::2]: # 2칸씩 건너 뛰어서 값 가져오기
    print("a" + str(i), end=" ") # 1, 3, 5, 7, ...

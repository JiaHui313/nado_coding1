#행맨hangman 게임 프로그램
#리스트에 3개 이상의 단어를 추가 -> list.append()사용
# 예) apple, bananan, orange 

# 위 리스트에서 랜덤으로 1개의 단어 선택 -> random()함수 사용

# 단어의 길이에 맞게 밑줄 출력 -> len()함수 사용

# 사용자로부터 1글자씩 입력을 받되,
# 단어에 입력값이 포함되면 "Correct"출력, 아니면 "Wrong"출력

# 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시(맞히지 못한 글자는 밑줄출력)
# a입력시: a _ _ _ _
# p입력시: a p p _ _
# c입력시: a p p _ _

# 정답을 맞히면 Success 출력 후 프로그램 종료(횟수 제한 없음)

from random import *
words = ["apple", "banana", "orange"]
word = choice(words)
print("answer: "+ word)
letters = "" #사용자로부터 지금까지 입력받은 단어 저장

while True:
# 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시(맞히지 못한 글자는 밑줄출력)
	succed = True
	print()
	for w in word: # a p p l e
		if w in letters:
			print(w, end= " ")
		else:
			print("_", end = " ")
			succed = False
	print()

	if succed:
		print("Success")
		break
	
	letter = input("Input letter: ")# 사용자로부터 입력받기
	if letter not in letters:
		letters += letter
	
	if letter in word:
		print("Correct")
	else:
		print("Wrong")

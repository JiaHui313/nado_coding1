from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로

txt = Text(root, width=30, height=5) #텍스트 위젯 만들기
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #엔터입력이 불가, 한줄로만 입력받을 때, 로그인, 닉네임같은 경우에 사용
e.pack()
e.insert(0, "한줄만 입력해요") #기본값 설정

def btncmd():
    #내용출력
    print(txt.get("1.0", END)) #1행, 0열부터 끝까지 가져오기
    print(e.get())
    #내용 삭제
    txt.delet("1.0", END) 
    e.delete(0, END)

btn= Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않도록

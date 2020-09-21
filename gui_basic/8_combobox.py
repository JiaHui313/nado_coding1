import tkinter.ttk as ttk
from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로

values = [str(i) +"일" for i in range(1, 32)] # 1~31까지 숫자
combobox = ttk.Combobox(root, height=5, values=values,)
combobox.pack()
combobox.set("카드 결제일") #최초 목록의 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #선택만 가능, 사용자입력 불가능
readonly_combobox.current(0) #0번째 인덱스 값 선택함.
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) #선택된 값 출력
    print(readonly_combobox.get())
   

btn= Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않도록

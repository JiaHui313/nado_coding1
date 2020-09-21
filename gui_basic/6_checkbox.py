from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로

chkvar = IntVar() #체크바에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동처리, 기본으로 체크가 된 상태임
# chkbox.deselect() #선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) #체크박스 값이-> 0: 체크해제, 1: 체크됨
    print(chkvar2.get())

btn= Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않도록

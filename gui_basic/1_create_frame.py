from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로
#root.geometry("640x480+300+100") #가로, 세로, x좌표, y좌표
root.resizable(False, False) #창크기 변경 불가, x너비, y너비

root.mainloop() #창이 닫히지 않도록

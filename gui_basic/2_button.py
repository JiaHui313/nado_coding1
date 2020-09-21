from tkinter import *

root =Tk()
root.title("GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() #pack()을 호출해야 버튼이 보임

btn2 = Button(root, padx= 5, pady=10, text="버튼222222") #padx:버튼가로사이즈, pady: 버튼세로사이즈
btn2.pack() #글자가 커지면 너비가 유동적으로 넓어짐

btn3 = Button(root, padx= 10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width = 10, height=3, text="버튼444444")#버튼 크기 고정적
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png") #이미지를 사용해서 버튼 만들기
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")
    
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #창이 닫히지 않도록

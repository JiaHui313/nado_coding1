from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480")
#레이블 만들기
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change(): #버튼 클릭 시 이미지 바꾸는 함수
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image = photo2)

btn = Button(root, text="click", command = change)
btn.pack()

root.mainloop() #창이 닫히지 않도록

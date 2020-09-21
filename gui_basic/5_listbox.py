from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로
#리스트박스 위젯만들기
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #리스트항목삭제
    #listbox.delete(0) #맨 처음 항목 삭제 0, END(뒤부터)
    
    #갯수확인
    #print("리스트에는 ", listbox.size(), "개가 있습니다.")
    
    #항목확인(시작idx, 끝idx)
    #print("1번째부터 3번째까지 항목: ", listbox.get(0,2))
    
    #선택된 항목확인(위치로 반환: ex 1, 2, 3)
    print("선택된 항목: ", listbox.curselection())


btn= Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않도록

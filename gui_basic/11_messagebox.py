import tkinter.messagebox as msgbox
from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로

#기차 예매 시스템이라고 가정함.
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제오류가 발생했습니다.")

def okaycancel(): #사용자에게 ok/cancel 묻기
    msgbox.askokcancel("확인/취소", "해당좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel(): 
    msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")


def yesno(): 
    msgbox.askyesno("예/아니오", "해당좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel(): 
    response = msgbox.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다.\n 저장후 프로그램을 저장하시겠습니까?")
    #네: 저장 후 종료
    #아니오: 저장 않고 종료
    #취소: 프로그램 종료 취소(현재화면에서 계속 작업)
    print("응답: ", response) #true, false, none -> 1, 0, 그외
    if response == 1:
        print("yes")
    elif response ==0:
        print("no")
    else:
        print("cancel")


Button(root, command=info, text = "알림").pack()
Button(root, command=warn, text = "경고").pack()
Button(root, command=error, text = "에러").pack()

Button(root, command=okaycancel, text = "확인취소").pack()
Button(root, command=retrycancel, text = "재시도취소").pack()
Button(root, command=yesno, text = "예 아니오").pack()
Button(root, command=yesnocancel, text = "예 아니오 취소").pack()
root.mainloop() #창이 닫히지 않도록

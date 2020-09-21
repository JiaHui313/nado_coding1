from tkinter import *

root =Tk()
root.title("GUI")
root.geometry("640x480") #창 크기: 가로*세로

def create_new_file():
    print("새파일을 만듭니다.")

menu = Menu(root)

#File메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() #구분선
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu = menu_file)

#Edit메뉴 탭(빈값)
menu.add_cascade(labe="Edit")

#랭귀지 메뉴 추가(radio버튼을 통해서 택1)
menu_lang = Menu(root, tearoff=0)
menu_lang.add_radiobutton(label ="Python")
menu_lang.add_radiobutton(label ="Java")
menu_lang.add_radiobutton(label ="C+")
menu.add_cascade(label="Language", menu = menu_lang)

#체크박스 탭 추가
menu_view = Menu(root, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu = menu_view)

root.config(menu=menu)
root.mainloop() #창이 닫히지 않도록

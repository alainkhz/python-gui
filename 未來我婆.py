from tkinter import*
from PIL import ImageTk
from PIL import Image

# gui
win = Tk()  # 建立視窗
win.title("First Gui")
win.geometry("800x500")
win.iconbitmap("C:\game\icon.ico")
win.config(background="#272727")


def ok():
    x = en.get()
    if x == "未來我婆":
        lb.config(text="我的才對")
    else:
        print("???")


# lable
lb = Label(bg="#272727", fg="white", text="mirai my wife")
lb.pack()


# entry
en = Entry()
en.pack()


# button
img = Image.open("C:\game\GitHub\python-gui\mirai.png")
ph = ImageTk.PhotoImage(img)
b = Button(text="按鈕", image=ph,)
b.config(command=ok)
b.pack()


win.mainloop()  # 讓視窗不會消失

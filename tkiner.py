from tkinter import*
from PIL import ImageTk
from PIL import Image


win = Tk()  # 建立視窗
win.title("First Gui")
win.geometry("800x500")
win.iconbitmap("C:\game\icon.ico")
win.config(background="#272727")


def say_hi():
    print("HI")


im = Image.open("C:\game\GitHub\python-gui\mirai.png")
ph = ImageTk.PhotoImage(im)


b = Button(text="按鈕", image=ph,)
b.config(command=say_hi)
b.pack()

win.mainloop()  # 讓視窗不會消失

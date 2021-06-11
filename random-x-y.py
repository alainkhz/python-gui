from tkinter import*
from tkinter import font
import random  # 隨機資料
import pyperclip  # 剪貼簿
#////////////////////////////////////////////////////////////////#

# 視窗
win = Tk()
win.title("X Y Generator")
win.geometry("600x370+600+200")
win.config(bg="#272727")
win.iconbitmap("C:\game\icon.ico")

# title lable
title_lable = Label(text="X Y Generator")
title_lable.config(fg="skyblue", bg="#272727", font="微軟正黑體 30")
title_lable.pack()

# min lable
min_range = Label(text="Min range")
min_range.config(fg="white", bg="#272727", font="微軟正黑體 20")
min_range.pack()

# min entry
min_entry = Entry()
min_entry.pack()

#space lable
space_lable= Label(bg="#272727")
space_lable.pack()

# max lable
max_range = Label(text="Max range")
max_range.config(fg="white", bg="#272727", font="微軟正黑體 20")
max_range.pack()

# min entry
max_entry = Entry()
max_entry.pack()

#show X Y
x_show = Label(text="X:",fg="white", bg="#272727", font="微軟正黑體 15")
x_show.pack()
y_show = Label(text="Y:",fg="white", bg="#272727", font="微軟正黑體 15")
y_show.pack() 


#按鈕邏輯
def generator_xy ():
    min = int(min_entry.get())
    max = int(max_entry.get())
    x = str(random.randint(min, max))
    y = str(random.randint(min, max))
    x_show.config(text="X:"+x)
    y_show.config(text='Y:'+y)

#複製按鈕
def  copy():
    xy = x_show.cget("text")+" "+ y_show.cget("text")
    pyperclip.copy(xy)
    

#button generator
button_generator = Button(text="generator", command= generator_xy)
button_generator.config(width=10, height=2)
button_generator.pack()

#space2 lable
space_lable2= Label(bg="#272727")
space_lable2.pack()

#button copy
button_copy = Button(text="copy", command= copy)
button_copy.config(width=10, height=2)
button_copy.pack()


win.mainloop()

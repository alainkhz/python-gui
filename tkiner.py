from tkinter import*


win = Tk()  # 建立視窗
win.title("First Gui")
win.geometry("800x500")
win.iconbitmap("C:\game\icon.ico")
win.config(background="#272727")

img = PhotoImage(file="C:\game\icon.png")


btn = Button(text="按鈕")
#btn = tk.Button(bg = "skyblue")
#btn.config(width=15, height=5)
btn.config(image=img)
btn.pack()

win.mainloop()  # 讓視窗不會消失

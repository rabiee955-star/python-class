from tkinter import *
from random import choice
win=Tk()
win.resizable(0,0)
x=win.winfo_screenwidth()
y=win.winfo_screenheight()
win.geometry(f"500x500+{(x-500)//2}+{(y-500)//2}")
win.title("Change color with events")
#widgets
lbl_title=Label(win,text="",font="Aptos 20")
lbl_title.pack(side=TOP,pady=10)
#functions
def click_1_color(event):
    win.config(background="#0000FF")
    lbl_title.config(text="Left_click",bg="#0000FF")
def click_3_color(event):
    win.config(background="#FFFF00")
    lbl_title.config(text="Right_click",bg="#FFFF00")
def enter_color(event):
    win.config(background="#00FF00")
    lbl_title.config(text="Enter",bg="#00FF00")
def change_color_1_16(event):
    parts = "0123456789ABCDEF"
    num_1=""
    for i in range(6):
        num=choice(parts)
        num_1+=num
    exit_color=f"#{num_1}"
    win.config(background=exit_color)
    lbl_title.config(text="Key",bg=exit_color)
win.bind("<Button-1>",click_1_color)
win.bind("<Button-3>",click_3_color)
win.bind("<Return>",enter_color)
win.bind("<Key>",change_color_1_16)
win.mainloop()
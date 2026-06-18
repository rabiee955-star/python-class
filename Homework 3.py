from tkinter import *
from tkinter import messagebox
from random import choice,randint
win=Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("Game color")
colors=["red","green","blue","yellow","orange","purple","pink","brown","black","white"]
time=60
score=0
#functions
def start(event):
    ent_color.focus_set()
    if time==60:
        countdown()
    color()
def countdown():
    global time,score
    if time > 0:
        lbl_time.config(text= f"time={time}")
        time-=1
        lbl_time.after(1000,countdown)
    if time==0:
        messagebox.showerror("Game color",f"End time \n Your score is : {score}")
current_color = ""
def color():
    global colors, score, current_color
    user = ent_color.get().lower()
    if user != "":
        if user == current_color.lower():
            score += 10
        else:
            score -= 5
        lbl_score.config(text=str(score))
    ent_color.delete(0, END)
    color_1 = colors[randint(0,len(colors)-1)]
    color_name = colors[randint(0,len(colors)-1)]
    current_color = color_1
    lbl_color.config(text=color_name, fg=color_1)
#widgets
lbl_score=Label(win , text=str(0),font="Aptos 30")
lbl_score.place(x=10,y=10)
lbl_title=Label(win,text="Enter the color of name:",font="Aptos 20").pack(side=TOP,pady=10)
lbl_sat=Label(win,text="Click Enter to start:",font="Aptos 20")
lbl_sat.pack(side=TOP,pady=10)
lbl_time=Label(win,text= f"time={time}",font="Aptos 20")
lbl_time.pack(side=TOP,pady=10)
lbl_color=Label(win,text="",font="Aptos 50")
lbl_color.pack(side=TOP,pady=10)
ent_color=Entry(win,font="Aptos 20")
ent_color.pack(side=BOTTOM,pady=100)
win.bind("<Return>",start)
win.mainloop()
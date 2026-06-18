from tkinter import *
from tkinter import messagebox
from decimal import Decimal
win=Tk()
win.resizable(0,0)
x=win.winfo_screenwidth()
y=win.winfo_screenheight()
win.geometry(f"500x500+{(x-500)//2}+{(y-500)//2}")
win.title("Timer")
time=0
h="00"
m="00"
s="00"
ms="0"
standard_time="00:00:00.0"
#function
def Set():
    global time,h,m,s,ms,standard_time
    time = Decimal(ent_time.get())
    h=str(time // 3600)
    if int(h) < 10:
        h="0"+h
    m=str(((time % 3600) // 60))
    if int(m) < 10:
        m="0"+m
    s=str(((time%3600)%60)//1)
    if int(s) <10:
        s="0"+s
    ms=str(time%1)
    if int(ms) < 10:
        ms="00"+ms
    if 10<int(ms) < 100:
        ms="0"+ms
    standard_time = f"{h}:{m}:{s}.{ms}"
    if -time.as_tuple().exponent > 1:
        messagebox.showerror("Error","Input must have less or equal to 1 decimal places ")
        time=0
        ent_time.delete(0, END)
        lbl_time.config(text=time)
    else:
        lbl_time.config(text=standard_time)
        ent_time.delete(0,END)
        return(time)
def Start():
    global time, h, m, s, ms, standard_time
    h = str(time // 3600)
    if int(h) < 10:
        h = "0" + h
    m = str(time % 3600 // 60)
    if int(m) < 10:
        m = "0" + m
    s = str(((time % 3600) % 60) // 1)
    if int(s) < 10:
        s = "0" + s
    ms = str(int((Decimal(time % 1))*1000))
    if int(ms) < 10:
        ms="00"+ms
    standard_time = f"{h}:{m}:{s}.{ms}"
    if time > 0:
        btn_set.config(state=DISABLED)
        btn_start.config(state=DISABLED)
        ent_time.config(state=DISABLED)
        lbl_time.config(text=standard_time)
        time-=Decimal("0.1")
        lbl_time.after(100,Start)
        if time ==0:
            lbl_time.config(text="00:00:00.000")
            messagebox.showinfo("Timer","End time ")
            btn_set.config(state=NORMAL)
            btn_start.config(state=NORMAL)
            ent_time.config(state=NORMAL)
def Reset():
    global time
    time=0
    ent_time.delete(0,END)
    lbl_time.config(text=time)
    btn_set.config(state=NORMAL)
    btn_start.config(state=NORMAL)
    ent_time.config(state=NORMAL)
#widget
lbl_input=Label(win,text="Enter the time (s) : ")
lbl_input.place(x=10,y=10)
ent_time=Entry(win)
ent_time.place(x=120,y=10)
btn_set=Button(win,text="Set time",width=20,command=Set)
btn_set.place(x=10,y=450)
btn_start=Button(win,text="Start",width=20,command=Start)
btn_start.place(x=170,y=450)
btn_reset=Button(win,text="Reset",width=20,command=Reset)
btn_reset.place(x=330,y=450)
lbl_time=Label(win,text='0',font="Aptos 50")
lbl_time.pack(side=TOP,pady=180)
win.mainloop()
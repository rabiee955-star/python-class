from tkinter import *
import functions
from tkinter import messagebox
win=Tk()
win.geometry("400x500")
#functions
functions.create()
def sub():
    username=ent_u.get()
    password=ent_p.get()
    functions.insert(username, password)
    messagebox.showinfo("Submit","This user submited")
    clear()
def clear():
    ent_p.delete(0,END)
    ent_u.delete(0,END)
    ent_u.focus_set()
def exit():
    ask_exit=messagebox.askquestion("Exit","Do you want exit ?")
    if ask_exit=="yes":
        win.destroy()
def show():
    lst_user.delete(0,END)
    for record in functions.show_user():
        lst_user.insert(END,record)
#widgets
lbl_u=Label(win,text="Username : ",font="Aptos 15")
lbl_u.place(x=10,y=10)
lbl_p=Label(win,text="Password : ",font="Aptos 15")
lbl_p.place(x=10,y=50)
ent_u=Entry(win,font="Aptos 15")
ent_u.place(x=120,y=10)
ent_p=Entry(win,show="*",font="Aptos 15")
ent_p.place(x=120,y=50)
btn_s=Button(win,text="Submit",font="Aptos 10",width=22,command=sub)
btn_s.place(x=10,y=150)
btn_c=Button(win,text="Cancel",font="Aptos 10",width=22,command=exit)
btn_c.place(x=202,y=150)
btn_show=Button(win,text="Show",font="Aptos 10",width=46,command=show)
btn_show.place(x=10,y=180)
lst_user=Listbox(win,font="Aptos 10",width=54,height=15)
lst_user.place(x=10,y=220)
win.mainloop()
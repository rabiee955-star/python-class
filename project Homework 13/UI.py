import Backend
from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("600x400")
db_path="E:/LOST.DIR/project Homework 13/database.db"
db=Backend.Database(db_path)
#functions
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
def sign_up():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if email=="" or password == "":
        messagebox.showerror("Error","Email or password are empty")
        clear()
        return
    clear()
    record = db.search(email,password)
    if record :
        messagebox.showerror("Error","You should Sign in ! No Sign up")
        return
    db.sign_up(fname,lname,email,password)
    messagebox.showinfo("Sign Up","This user Signed up")
def sign_in():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    record = db.search(email,password)
    clear()
    if record:
        print(record)
        tpl=Toplevel(win)
        lbl_title=Label(tpl,text=f"Wlecome {record[0][1],record[0][2]}\n{record[0]}")
        lbl_title.place(x=20,y=20)
#widgets
lbl_fname=Label(win,text="Fname :",font="Aptos 20")
lbl_fname.place(x=40,y=40)
ent_fname=Entry(win,font="Aptos 20")
ent_fname.place(x=200,y=40)
lbl_lname=Label(win,text="Lname :",font="Aptos 20")
lbl_lname.place(x=40,y=100)
ent_lname=Entry(win,font="Aptos 20")
ent_lname.place(x=200,y=100)
lbl_email=Label(win,text="*Email :",font="Aptos 20")
lbl_email.place(x=40,y=160)
ent_email=Entry(win,font="Aptos 20")
ent_email.place(x=200,y=160)
lbl_password=Label(win,text="*Password :",font="Aptos 20")
lbl_password.place(x=40,y=220)
ent_password=Entry(win,font="Aptos 20")
ent_password.place(x=200,y=220)
btn_sign_up=Button(win,text="Sign Up",font="Aptos 20",command=sign_up)
btn_sign_up.place(x=40,y=300)
btn_sign_in=Button(win,text="Sign In",font="Aptos 20",command=sign_in)
btn_sign_in.place(x=200,y=300)
win.mainloop()
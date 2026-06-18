from tkinter import *
import backend
from tkinter import messagebox
win=Tk()
win.geometry("400x500")
#functions
db=backend.Database("I:/LOST.DIR/project/myfile.db")
def sub():
    username=ent_u.get()
    password=ent_p.get()
    if username=="" or password=="":
        messagebox.showerror("Error","Username or Password are empty.")
        clear()
    else:
        for record in db.select_user():
            if username == record[1] and password == record[2]:
                messagebox.showinfo("Error","This User is already registered.")
                return
        db.insert_user(username,password)
        messagebox.showinfo("Submit","This user submited")
        clear()
def clear():
    ent_p.delete(0,END)
    ent_u.delete(0,END)
    ent_u.focus_set()
def exit():
    result_exit=messagebox.askquestion("Exit","Do you want exit ?")
    if result_exit=="yes":
        win.destroy()
def show():
    lst_user.delete(0,END)
    for record in db.select_user():
        lst_user.insert(END,f"{record[0]}  {record[1]}  {record[2]}")
def show_check():
    #functions
    def password_show():
        counter_false=0
        pass_entry=ent_pass.get()
        pass_original=db.owner()[2]
        if pass_entry == pass_original:
            show()
            tpl_show.destroy()
        else:
            tpl_show.destroy()
            messagebox.showerror("Error","Password not match")
    #widgets
    tpl_show=Toplevel(win)
    tpl_show.geometry("600x400")
    tpl_show.title("password for show")
    lbl_pass=Label(tpl_show,text="Enter the President password : ",font="Aptos 15")
    lbl_pass.place(x=20,y=20)
    ent_pass=Entry(tpl_show,font="Aptos 15",show="*")
    ent_pass.place(x=320,y=20)
    btn_pass=Button(tpl_show,text="Show",command=password_show)
    btn_pass.pack(pady=10,side=BOTTOM)
def delete():
    index=lst_user.curselection()
    data=lst_user.get(index)
    result=messagebox.askquestion("Delete","Do you want to delete this user ?")
    if result=="yes":
        db.delete_user(data[0])
        show()
#widgets
lbl_u=Label(win,text="*Username : ",font="Aptos 15")
lbl_u.place(x=10,y=10)
lbl_p=Label(win,text="*Password : ",font="Aptos 15")
lbl_p.place(x=10,y=50)
ent_u=Entry(win,font="Aptos 15")
ent_u.place(x=120,y=10)
ent_p=Entry(win,show="*",font="Aptos 15")
ent_p.place(x=120,y=50)
btn_s=Button(win,text="Submit",font="Aptos 10",width=22,command=sub)
btn_s.place(x=10,y=120)
btn_e=Button(win,text="Exit",font="Aptos 10",width=22,command=exit)
btn_e.place(x=202,y=120)
btn_show=Button(win,text="Show",font="Aptos 10",width=46,command=show_check)
btn_show.place(x=10,y=150)
btn_delete=Button(win,text="Delete",font="Aptos 10",width=46,command=delete)
btn_delete.place(x=10,y=180)
lst_user=Listbox(win,font="Aptos 10",width=54,height=15)
lst_user.place(x=10,y=220)
win.mainloop()
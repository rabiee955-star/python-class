from tkinter import *
from tkinter import messagebox
import Backend
font='arial 12 bold'
sb_c="skyblue"
o_c="orange"
win= Tk()
win.title('Homework 11')
win.geometry('800x600')
win.resizable(0,0)
win.configure(bg=sb_c)
db_path="I:/LOST.DIR/project Homework 11/database.db"
db=Backend.Database(db_path)
#functions
def insert():
    fname=ent_fname.get()
    lname=ent_lname.get()
    address=ent_address.get()
    phone=ent_phone.get()
    if fname == "" or lname == "":
        messagebox.showerror("Error","Fname or Lname are empty.")
    else:
        db.insert_user(fname,lname,address,phone)
        messagebox.showinfo("Submit","This user submited")
    clear()
    show()
def show():
    lst_user.delete(0,END)
    records=db.show_user()
    for record in records:
        lst_user.insert(END,record)

def delete():
    index=lst_user.curselection()
    data=lst_user.get(index)
    result=messagebox.askquestion("Delete","Do you want to delete this user ?")
    if result=="yes":
        db.delete_user(data[0])
        show()
        clear()
def search():
    lst_user.delete(0,END)
    search=ent_search.get()
    
    if "%" in search or "_" in search :
        search_val=str(search)
    else :
        search_val=f"%{search}%"
    if search == "" :
        messagebox.showerror("Error","The search entry is empty.")
    records_search=db.search_user(search_val)
    for record_search in records_search:
        lst_user.insert(END,record_search)
def search_2(event):
    lst_user.delete(0,END)
    search_2=ent_search_2.get()
    search_val_2=f"{search_2}%"
    records_search=db.search_user_2(search_val_2)
    for record_search in records_search:
        lst_user.insert(END,record_search)
def fetch(event):
    clear()
    index=lst_user.curselection()
    data=lst_user.get(index)
    ent_fname.insert(0,data[1])
    ent_lname.insert(0,data[2])
    ent_address.insert(0,data[3])
    ent_phone.insert(0,data[4])
def update():
    index=lst_user.curselection()
    data=lst_user.get(index)
    db.update_user(data[0],ent_fname.get(),ent_lname.get(),ent_address.get(),ent_phone.get())
    show()
    clear()
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)
    ent_fname.focus_set()
def exit():
    result_exit=messagebox.askquestion("Exit","Do you want exit ?")
    if result_exit=="yes":
        win.destroy()
#widgets
lbl_fname=Label(win,font=font,text='Fname: ',bg=sb_c)
lbl_fname.place(x=80,y=10)
lbl_lname=Label(win,font=font,text='Lname: ',bg=sb_c)
lbl_lname.place(x=450,y=10)
lbl_address=Label(win,font=font,text='Address: ',bg=sb_c)
lbl_address.place(x=80,y=50)
lbl_phone=Label(win,font=font,text='Phone: ',bg=sb_c)
lbl_phone.place(x=450,y=50)
ent_fname=Entry(win,font='arial 10',width=27)
ent_fname.place(x=180,y=12)
ent_lname=Entry(win,font='arial 10',width=27)
ent_lname.place(x=550,y=12)
ent_address=Entry(win,font='arial 10',width=27)
ent_address.place(x=180,y=52)
ent_phone=Entry(win,font='arial 10',width=27)
ent_phone.place(x=550,y=52)
btn_insert=Button(win,font=font,bg=o_c,width=10,text='Insert',command=insert)
btn_insert.place(x=110,y=130)
btn_show_list=Button(win,font=font,bg=o_c,width=10,text='Show List',command=show)
btn_show_list.place(x=110,y=180)
btn_delete=Button(win,font=font,bg=o_c,width=10,text='Delete',command=delete)
btn_delete.place(x=240,y=130)
btn_search=Button(win,font=font,bg=o_c,width=10,text='Search',command=search)
btn_search.place(x=240,y=180)
btn_update=Button(win,font=font,bg=o_c,width=10,text='Update',command=update)
btn_update.place(x=370,y=130)
btn_clear=Button(win,font=font,bg=o_c,width=10,text='Clear',command=clear)
btn_clear.place(x=500,y=130)
btn_exit=Button(win,font=font,bg=o_c,width=10,text='Exit',command=exit)
btn_exit.place(x=630,y=130)
ent_search=Entry(win,font='arial 10',width=20)
ent_search.place(x=360,y=185)
scroll_listbox=Scrollbar(win)
scroll_listbox.place(x=30,y=280,height=212,width=20)
lst_user=Listbox(win,font='arial 10',width=75,height=12,yscrollcommand=scroll_listbox.set)
lst_user.place(x=55,y=280)
lst_user.bind("<<ListboxSelect>>",fetch)
lbl_search=Label(win,text="Enter name for search :",bg=sb_c,font=font)
lbl_search.place(x=80,y=225)
ent_search_2=Entry(win,font='arial 10',width=27)
ent_search_2.place(x=280,y=225)
ent_search_2.bind("<KeyRelease>",search_2)
win.mainloop()
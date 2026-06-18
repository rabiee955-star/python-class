from tkinter import *
from tkinter import messagebox
import Backend
win=Tk()
win.geometry("600x400")
db_path="E:/python_Homework 3/project Homework 14/Data.db"
db=Backend.Database(db_path)
#funtions
def show():
    clear()
    lst.delete(0,"end")
    records=db.show_commodity()
    for record in records:
        lst.insert("end",record)
def clear():
    ent_buy.delete(0,"end")
    ent_sell.delete(0,"end")
    ent_number.delete(0,"end")
    ent_name.delete(0,"end")
def add():
    name=ent_name.get()
    buy=ent_buy.get()
    sell=ent_sell.get()
    number=ent_number.get()
    if name!="" and buy!="" and sell!="" and number!="":
        db.add_commodity(name,buy,sell,number)
        show()
        messagebox.showinfo("commodity","This commodity submited")
    else:
        messagebox.showerror("commodity", "Entrys are empty")
        show()
def search():
    lst.delete(0,"end")
    name = ent_name.get()
    buy = ent_buy.get()
    sell = ent_sell.get()
    number = ent_number.get()
    records=db.search_commodity(name,buy,sell,number)
    if records:
        for record in records:
            lst.insert("end",record)
    else:
        messagebox.showinfo("commodity","Not found records")
def fetch(event):
    index=lst.curselection()
    data=lst.get(index)
    ent_name.insert("end",data[1])
    ent_buy.insert("end",data[2])
    ent_sell.insert("end",data[3])
    ent_number.insert("end",data[4])
def delete():
    index=lst.curselection()
    data=lst.get(index)
    result=messagebox.askquestion("Delete","Do you want to delete this user ?")
    if result=="yes":
        db.delete_commodity(data[0])
        show()
def update():
    name = ent_name.get()
    buy = ent_buy.get()
    sell = ent_sell.get()
    number = ent_number.get()
    index=lst.curselection()
    data=lst.get(index)
    db.update_commodity(data[0],name,buy,sell,number)
    show()
def exit():
    result_exit=messagebox.askquestion("Exit","Do you want exit ?")
    if result_exit=="yes":
        win.destroy()
#wigets
lbl_name=Label(win,text="نام کالا :")
lbl_name.place(x=10,y=10)
ent_name=Entry(win)
ent_name.place(x=90,y=10)
lbl_buy=Label(win,text="قمیت خرید :")
lbl_buy.place(x=200,y=10)
ent_buy=Entry(win)
ent_buy.place(x=280,y=10)
lbl_sell=Label(win,text="قیمت فروش :")
lbl_sell.place(x=10,y=50)
ent_sell=Entry(win)
ent_sell.place(x=90,y=50)
lbl_number=Label(win,text="تعداد :")
lbl_number.place(x=200,y=50)
ent_number=Entry(win)
ent_number.place(x=280,y=50)
wid=20
btn_add=Button(win,text="اضافه کردن",width=wid,command=add)
btn_add.place(x=440,y=10)
btn_search=Button(win,text="جستوجو کالا",width=wid,command=search)
btn_search.place(x=440,y=40)
btn_delete=Button(win,text="حذف کالا",width=wid,command=delete)
btn_delete.place(x=440,y=70)
btn_update=Button(win,text="ویرایش",width=wid,command=update)
btn_update.place(x=440,y=100)
btn_exit=Button(win,text="بستن",width=wid,command=exit)
btn_exit.place(x=440,y=130)
lst=Listbox(win,height=18,width=70)
scroll=Scrollbar(win)
lst.place(x=10,y=75)
scroll=Scrollbar(win,orient=VERTICAL)
scroll.place(x=440,y=160,height=180)
scroll.config(command=lst.yview)
lst.config(yscrollcommand=scroll.set)
lst.bind("<<ListboxSelect>>",fetch)
win.mainloop()
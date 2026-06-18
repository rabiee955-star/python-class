from tkinter import *
from tkinter import messagebox
import Backend
win=Tk()
win.geometry("600x400")
db_path="E:/python_Homework 3/project Homework 15/Data.db"
db=Backend.Database(db_path)
#funtions
def show():
    clear()
    lst.delete(0,"end")
    records=db.show_book()
    for record in records:
        lst.insert("end",record)
def clear():
    ent_writer.delete(0,"end")
    ent_year.delete(0,"end")
    ent_number.delete(0,"end")
    ent_name.delete(0,"end")
def add():
    name=ent_name.get()
    writer=ent_writer.get()
    year=ent_year.get()
    number=ent_number.get()
    if name!="" and writer!="" and year!="" and number!="":
        db.add_book(name,writer,year,number)
        show()
        messagebox.showinfo("book","This book submited")
    else:
        messagebox.showerror("book", "Entrys are empty")
        show()
def search():
    lst.delete(0,"end")
    name = ent_name.get()
    writer = ent_writer.get()
    year = ent_year.get()
    number = ent_number.get()
    records=db.search_book(name,writer,year,number)
    if records:
        for record in records:
            lst.insert("end",record)
    else:
        messagebox.showinfo("book","Not found records")
def fetch(event):
    ent_writer.delete(0,"end")
    ent_year.delete(0,"end")
    ent_number.delete(0,"end")
    ent_name.delete(0,"end")
    index=lst.curselection()
    data=lst.get(index)
    ent_name.insert("end",data[1])
    ent_writer.insert("end",data[2])
    ent_year.insert("end",data[3])
    ent_number.insert("end",data[4])
def delete():
    index=lst.curselection()
    data=lst.get(index)
    result=messagebox.askquestion("Delete","Do you want to delete this book ?")
    if result=="yes":
        db.delete_book(data[0])
        show()

def exit():
    result_exit=messagebox.askquestion("Exit","Do you want exit ?")
    if result_exit=="yes":
        win.destroy()
#wigets
lbl_name=Label(win,text="عنوان:")
lbl_name.place(x=10,y=10)
ent_name=Entry(win)
ent_name.place(x=90,y=10)
lbl_writer=Label(win,text=" نویسنده:")
lbl_writer.place(x=200,y=10)
ent_writer=Entry(win)
ent_writer.place(x=280,y=10)
lbl_year=Label(win,text="سال انتشار:")
lbl_year.place(x=10,y=50)
ent_year=Entry(win)
ent_year.place(x=90,y=50)
lbl_number=Label(win,text="ISBN:")
lbl_number.place(x=200,y=50)
ent_number=Entry(win)
ent_number.place(x=280,y=50)
wid=20
btn_show=Button(win,text="مشاهده همه",width=wid,command=show)
btn_show.place(x=440,y=10)
btn_search=Button(win,text="جستوجو ی کتاب",width=wid,command=search)
btn_search.place(x=440,y=40)
btn_add=Button(win,text="افزودن کتاب",width=wid,command=add)
btn_add.place(x=440,y=70)
btn_delete=Button(win,text="حذف کردن",width=wid,command=delete)
btn_delete.place(x=440,y=100)
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
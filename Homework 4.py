from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("500x500")
#functions
def score():
    sc=0
    if i_python.get()==1:
        sc+=50
    if i_c.get()==1:
        sc+=30
    if i_java.get()==1:
        sc+=20
    lbl_score.config(text=f"Your score is : {str(sc)}")
#widgets
lblfr_lang=LabelFrame(win,text="Language program",bd=3,relief=GROOVE)
lblfr_lang.pack(padx=10,pady=10,fill=BOTH)    
i_python=IntVar()
i_c=IntVar()
i_java=IntVar()
chk_p=Checkbutton(lblfr_lang,text="Python",variable=i_python)
chk_p.pack(padx=20,side=LEFT)
chk_c=Checkbutton(lblfr_lang,text="C#",variable=i_c)
chk_c.pack(padx=20,side=LEFT)
chk_j=Checkbutton(lblfr_lang,text="Java",variable=i_java)
chk_j.pack(padx=20,side=LEFT)
btn_lang=Button(win,text="Show score",command=score)
btn_lang.pack(pady=10)
fr=Frame(win,bd=4,relief=GROOVE)
fr.pack(padx=10,pady=10,fill=BOTH)
lbl_score=Label(fr,text="",fg="red",font=("comic sans ms",30))
lbl_score.pack(padx=10)
win.mainloop()
import sqlite3
con=sqlite3.connect('E:/myfile.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS teachers(fname TEXT,lname TEXT,rights INEGER)")
con.commit()
for i in range(2):
    fname=input("Enter fname :")
    lname=input("Enter lname :")
    rights=input("Enter rights :")
    cur.execute("INSERT INTO teachers(fname,lname,rights) VALUES (?,?,?)",(fname,lname,rights))
    con.commit()
    print("Record Inserted")
con.close()
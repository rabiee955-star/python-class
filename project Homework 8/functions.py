import sqlite3
con=sqlite3.connect("I:/LOST.DIR/project/myfile.db")
cur=con.cursor()
def create():
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,username TEXT,password TEXT)")
    con.commit()
def insert(username,password):
    cur.execute("INSERT INTO user (id,username,password) VALUES (NULL,?,?)",(username,password))
    con.commit()
def show_user():
    cur.execute("SELECT * FROM user")
    records=cur.fetchall()
    return records
create()
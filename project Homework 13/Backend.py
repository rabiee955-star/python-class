import sqlite3
class Database():
    def __init__(self,db_path):
        self.con=sqlite3.connect(db_path)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,email TEXT,password TEXT)")
        self.con.commit
    def sign_up(self,fname,lname,email,password):
        self.cur.execute("INSERT INTO user (id,fname,lname,email,password) values(NULL,?,?,?,?)",(fname,lname,email,password))
        self.con.commit()
    def search(self,email,password):
        self.cur.execute("SELECT * FROM user WHERE email=? and password=?",(email,password))
        return self.cur.fetchall()



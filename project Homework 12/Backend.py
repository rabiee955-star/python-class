import sqlite3
class Database():
    def __init__(self,db_path):
        self.con=sqlite3.connect(db_path)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,address TEXT,phone INTEGER)")
        self.con.commit()
    def insert_user(self,fname,lname,address,phone):
        self.cur.execute("INSERT INTO user (id,fname,lname,address,phone) values(NULL,?,?,?,?)",(fname,lname,address,phone))
        self.con.commit()
    def show_user(self):
        self.cur.execute("SELECT * FROM user")
        records=self.cur.fetchall()
        return records
    def delete_user(self,id):
        self.cur.execute("DELETE from user WHERE id=?",(id,))
        self.con.commit()
    def update_user(self,id,new_fname,new_lname,new_address,new_phone):
        self.cur.execute("UPDATE user SET fname=?,lname=?,address=?,phone=? Where id =?",(new_fname,new_lname,new_address,new_phone,id))
        self.con.commit()
    def search_user(self,search):
        self.cur.execute("SELECT * FROM user WHERE fname like ? or lname like ? or address like ? or phone like ? ",(search,search,search,search))
        return self.cur.fetchall()
    def search_user_2(self,search):
        self.cur.execute("SELECT * FROM user WHERE fname like ?",(search,))
        return self.cur.fetchall()
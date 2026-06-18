import sqlite3
class Database:
    def __init__(self,db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,username TEXT,password TEXT)")
        self.con.commit()
    def insert_user(self,username,password):
        self.cur.execute("INSERT INTO user (id,username,password) VALUES (NULL,?,?)",(username,password))
        self.con.commit()
    def select_user(self):
        self.cur.execute("SELECT * FROM user")
        records=self.cur.fetchall()
        return records
    def delete_user(self,id):
        self.cur.execute("DELETE FROM user WHERE id = ?",(id,))
        self.con.commit()
    def owner(self):
        self.cur.execute("SELECT * FROM user WHERE id=1")
        owner = self.cur.fetchone()
        return owner
    def update_user(self,id,new_username,new_password):
        self.cur.execute("UPDATE user SET username = ? , password = ? WHERE id = ?"
        ,(new_username,new_password,id))
        self.con.commit()
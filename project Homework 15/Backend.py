import sqlite3
class Database:
    def __init__(self,db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,name TEXT,purchase_price INTEGER,selling_price INTEGER,number INTEGER)")
        self.con.commit()
    def add_book(self,name,purchase_price,selling_price,number):
        self.cur.execute("INSERT INTO book (name,purchase_price,selling_price,number) VALUES (?,?,?,?)",(name,purchase_price,selling_price,number))
        self.con.commit()
    def search_book(self,name,purchase_price,selling_price,number):
        self.cur.execute("SELECT * FROM book WHERE name =? or purchase_price =? or selling_price =? or number =?",(name,purchase_price,selling_price,number))
        self.con.commit()
        return self.cur.fetchall()
    def delete_book(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.con.commit()
    def show_book(self):
        self.cur.execute("SELECT * FROM book")
        self.con.commit()
        return self.cur.fetchall()
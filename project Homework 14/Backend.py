import sqlite3
class Database:
    def __init__(self,db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS commodity (id INTEGER PRIMARY KEY,name TEXT,purchase_price INTEGER,selling_price INTEGER,number INTEGER)")
        self.con.commit()
    def add_commodity(self,name,purchase_price,selling_price,number):
        self.cur.execute("INSERT INTO commodity (name,purchase_price,selling_price,number) VALUES (?,?,?,?)",(name,purchase_price,selling_price,number))
        self.con.commit()
    def search_commodity(self,name,purchase_price,selling_price,number):
        self.cur.execute("SELECT * FROM commodity WHERE name =? or purchase_price =? or selling_price =? or number =?",(name,purchase_price,selling_price,number))
        self.con.commit()
        return self.cur.fetchall()
    def delete_commodity(self,id):
        self.cur.execute("DELETE FROM commodity WHERE id = ?",(id,))
        self.con.commit()
    def update_commodity(self,id,new_name,new_purchase_price,new_selling_price,new_number):
        self.cur.execute("UPDATE commodity SET name=?,purchase_price=?,selling_price=?,number=? WHERE id =?",(new_name,new_purchase_price,new_selling_price,new_number,id))
        self.con.commit()
    def show_commodity(self):
        self.cur.execute("SELECT * FROM commodity")
        self.con.commit()
        return self.cur.fetchall()
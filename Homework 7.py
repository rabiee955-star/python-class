import sqlite3
con=sqlite3.connect("database/myfile.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,salary INTEGER)")
con.commit()
for i in range(5):
    fname=input(f"Enter fname {i+1} : ")
    lname=input(f"Enter lname {i+1} : ")
    salary=input(f"Enter salary {i+1} : ")
    cur.execute("INSERT INTO employee (id,fname,lname,salary) VALUES (NULL,?,?,?)",(fname,lname,salary))
    con.commit()
    print("Record inserted")
cur.execute("SELECT * FROM employee")
records=cur.fetchall()
for record in records:
    print(f"code : {record[0]} -\t fname :{record[1]} \t lname :{record[2]} \t salary :{record[3]}")
print("The up employees are:")
cur.execute("Select * from employee WHERE salary>20000")
records_up=cur.fetchall()
for record_up in records_up:
     print(f"code : {record_up[0]} -\t fname :{record_up[1]} \t lname :{record_up[2]} \t salary :{record_up[3]}")
print(f"The number of up employees is : {len(records_up)}")
con.close()
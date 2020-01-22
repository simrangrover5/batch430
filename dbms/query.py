import sqlite3 as sql

db = sql.connect("employee.db")
c = db.cursor()

c.execute("select * from employee")

data = c.fetchall()    #fetchone() fetch single tuple
print(data)

for i in data:
    print("Id : ",i[0])
    print("Name : ",i[1])
    print("Address : ",i[2])

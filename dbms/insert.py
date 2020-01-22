import sqlite3 as sql


db = sql.connect("employee.db")

c = db.cursor()

#cmd = "create table employee(id integer,name varchar(200),address varchar(200))"

#c.execute(cmd)


while True:
    id1 =  int(input("Enter your id : "))
    name = input("Enter your name : ")
    add = input("Enter your address : ")

    cmd = "insert into employee values({},'{}','{}')".format(id1,name,add)
    c.execute(cmd)
    db.commit()
    print("Inserted successfully")
    ch = input("Do you want to continue(y/n) : ")
    if ch.lower() == "n":
        print("OKAY BYE")
        break

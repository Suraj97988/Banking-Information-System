import mysql.connector as mc

try:
    def createdatabase():
        con = mc.connect(host="localhost", user="root", password="Agarwal", use_pure=True)
        cur = con.cursor()
        createDatabase = "create database Bank"
        cur.execute(createDatabase)
        con.commit()
        print("Database created successfully")

except mc.DatabaseError as db:
    print("Database not connected")

try:
    def createtable():
        con = mc.connect(host="localhost", user="root", password="Agarwal",database="Bank", use_pure=True)
        cur = con.cursor()
        tq = "create table Banking(ACNO int primary key, CNAME varchar(30) not null,\
        BAL real not null, PIN int not null, BNAME varchar(30) not null)"
        cur.execute(tq)
        con.commit()
        print("Table created successfully")
except mc.DatabaseError as db:
    print("Database not connected")

#Main Program
# createdatabase()
# createtable()


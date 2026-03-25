#BankViewCustomers.py
import mysql.connector as mc
from BankExcept import CustomerNotFoundError
def viewcustomer():
    while True:
        try:
            con = mc.connect(host="localhost", user="root", password="Agarwal", database="bank")
            cur = con.cursor()
            acno = int(input("Enter your Account Number: "))
            pin = int(input("Enter your Pin Number: "))
            sq = "select * from banking where acno = %s and pin = %s"
            cur.execute(sq, (acno, pin))
            records = cur.fetchone()
            desc = cur.description
            print("\t\t Customer Details")
            for val in desc:
                print(f"\t\t{val[0]}",end = " ")
                # print()
            con.commit()
            if records[0] == acno and records[3] == pin:
                print()
                for record in records:
                    print(f"\t{record}", end = " ")
                print()
            else:
                raise CustomerNotFoundError
            ch = input("Do you wanna view more customer? (y/n) ")
            if ch.lower() == "n":
                break
        except mc.DatabaseError as db:
            print("Database Error", db)

def viewallcustomers():
    try:
        con = mc.connect(host="localhost", user="root", password="Agarwal", database="bank")
        cur = con.cursor()
        st = "show tables"
        cur.execute(st)
        tables = cur.fetchall()
        tables = tables[0]
        # search_table = input("Enter Table Name: ")
        sq = "select * from %s" % (tables)
        cur.execute(sq)
        records = cur.fetchall()
        desc = cur.description
        print("\t\t All Customer Details")
        for val in desc:
            print(f"\t\t{val[0]}", end=" ")
            # print()
        con.commit()
        if records:
            print()
            for record in records:
                for val in record:
                    print(f"\t{val}", end=" ")
                print()
        else:
            raise CustomerNotFoundError
    except mc.DatabaseError as db:
        print("Database Error", db)


# Main Program
# viewcustomer()
# viewallcustomers()
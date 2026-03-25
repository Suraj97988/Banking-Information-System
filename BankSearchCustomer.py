# BankSearchCustomer.py
import mysql.connector as mc
from BankExcept import CustomerNotFoundError
def searchcustomer():
    while True:
        try:
            con = mc.connect(host="localhost", user="root", password="Agarwal", database="bank", use_pure=True)
            cur = con.cursor()
            acno = int(input("Enter your Account Number: "))
            pin = int(input("Enter your Pin Number: "))
            sq = "select * from banking where acno = %s and pin = %s"
            cur.execute(sq, (acno, pin))
            records = cur.fetchone()
            con.commit()
            print(records)
            if records[0] == acno and records[3] == pin:
                print(f"Customer Account No :- {records[0]} \nName :- {records[1]} \nExist in Bank")
            else:
                raise CustomerNotFoundError
            ch = input("Do you want to search more customer (y/n)")
            if ch.lower() == "n":
                break

        except mc.DatabaseError as db:
            print("Database Error",db)


# Main Program
# searchcustomer()
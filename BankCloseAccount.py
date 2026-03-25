import mysql.connector as mc
from BankExcept import CustomerNotFoundError
def accountclose():
    while True:
        try:
            con = mc.connect(host="localhost", user="root", password="Agarwal", database="bank",use_pure=True)
            cur = con.cursor()
            acno = int(input("Enter Account Number to close: "))
            pin = int(input("Enter PIN Number: "))
            sq = "select * from banking where acno = %s and pin = %s"
            cur.execute(sq, (acno, pin))
            records = cur.fetchone()
            if records[0] == acno and records[3] == pin:
                dq = "delete from banking where acno = %s and pin = %s"
                cur.execute(dq, (acno, pin))
                con.commit()
                print("Account Closed Successfully")
            else:
                print("Account Number and Pin is wrong")
            ch = input("Do you want to close more? (yes/no)")
            if ch.lower() == "no":
                break
        except mc.DatabaseError as db:
            print("Database Not Connected ",db)
        except CustomerNotFoundError:
            print("Customer Not Found ")

# Main Program
# accountclose()

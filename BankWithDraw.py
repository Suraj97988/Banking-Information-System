# BankWithDraw.py<
#BankDeposit.py
from BankExcept import WithDrawError
import mysql.connector as mc
def withdraw():
    try:
        con = mc.connect(host="localhost", user="root", password="password", database="bank", use_pure=True)
        cur = con.cursor()

        acno = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN Number: "))
        amount = int(input("Enter Withdrwal Amount: "))
        sq = "select bal from banking where acno = %s and pin = %s"
        cur.execute(sq, (acno, pin))
        records = cur.fetchone()
        print(records[0])
        if records is None:
            print("❌ Invalid Account Number or PIN")
            return

        available_balance = records[0]
        withdraw_amount = available_balance - amount
        if amount <= available_balance:
            update_query = "UPDATE banking SET bal=%s WHERE acno=%s"
            cur.execute(update_query, (withdraw_amount, acno))
            con.commit()
            print("✅ Amount Withdraw:", amount)
            print("💰 New Balance:", withdraw_amount)
        else:
            raise WithDrawError("Insufficient Balance")
    except mc.DatabaseError as db:
        print("Database Not Connected",db)


# Main Program

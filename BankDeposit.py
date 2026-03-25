#BankDeposit.py
import mysql.connector as mc
def deposit():
    try:
        con = mc.connect(host="localhost", user="root", password="Agarwal", database="bank", use_pure=True)
        cur = con.cursor()

        acno = int(input("Enter Account Number: "))
        pin = int(input("Enter New PIN Number: "))
        amount = int(input("Enter Deposit Amount: "))
        sq = "select bal from banking where acno = %s and pin = %s"
        cur.execute(sq, (acno, pin))
        records = cur.fetchone()
        print(records)
        if records is None:
            print("❌ Invalid Account Number or PIN")
            return

        previosDeposit = records[0]
        newDeposit = amount + previosDeposit

        update_query = "UPDATE banking SET bal=%s WHERE acno=%s"
        cur.execute(update_query, (newDeposit, acno))
        con.commit()
        cur.execute(update_query, (newDeposit, acno))
        con.commit()
        print("✅ Amount Deposited:", amount)
        print("💰 New Balance:", newDeposit)
    except mc.DatabaseError as db:
        print("Database Not Connected",db)

# Main Program
# deposit()
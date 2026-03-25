import mysql.connector as mc
from BankExcept import PinLengthError
def pingenerate():
    try:
        con = mc.connect(host="localhost",user="root",password="Agarwal",database="bank",use_pure=True)
        cur = con.cursor()
        acno = int(input("Enter Account Number: "))
        sq = "select * from banking where acno = %s;" %(acno)
        cur.execute(sq)
        records = cur.fetchall()
        con.commit()
        if records[0][0] == acno:
            generatepin = int(input("Enter New PIN Number: "))
            if len(str(generatepin)) == 4:
                sq = "update banking set pin = %s where acno = %s" % (generatepin, acno)
                cur.execute(sq)
                con.commit()
                print("PIN Number Generated")
            else:
                print("PIN Number Should Be 4 Digits")
        print(records)

    except mc.DatabaseError as db:
        print("Database not connected",db)

def pinupdate():
    try:
        con = mc.connect(host="localhost",user="root",password="Agarwal",database="bank",use_pure=True)
        cur = con.cursor()
        acno = int(input("Enter Account Number: "))
        pin = int(input("Enter New PIN Number: "))
        sq = "select * from banking where acno = %s and pin = %s;" %(acno,pin)
        cur.execute(sq)
        records = cur.fetchall()
        con.commit()
        if records[0][0] == acno and records[0][3] == pin:
            generateNewPin = int(input("Enter New PIN Number: "))
            if len(str(generateNewPin)) == 4:
                sq = "update banking set pin = %s where acno = %s" % (generateNewPin, acno)
                cur.execute(sq)
                con.commit()
                print("PIN Number Updated")
            else:
                print("PIN Number Should Be 4 Digits")
        print(records)

    except mc.DatabaseError as db:
        print("Database not connected",db)

# Main Program
# pingenerate()
# pinupdate()


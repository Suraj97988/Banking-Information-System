# Bank Account Open
import mysql.connector as mc
from BankExcept import SpaceError,EmptyNameError,InvalidNameError
from validate import validate

def openaccount():
    while True:
        try:
            con = mc.connect(
                host="localhost",
                user="root",
                password="Agarwal",
                database="bank",
                use_pure=True
            )

            cur = con.cursor()

            acno = int(input("Enter Account Number: "))

            while True:
                cname = input("Enter Customer Name: ")
                try:
                    vname = validate(cname)
                except InvalidNameError:
                    print(f"\t{cname} is Invalid")
                except SpaceError:
                    print(f"\tDon't enter Space for name")
                except EmptyNameError:
                    print(f"\t{cname} is Empty")
                else:
                    print(f"\t{vname} is Valid Name")
                    break
            bal = float(input("Enter Balance: "))
            pin = int(input("Enter PIN Number: "))
            bname = input("Enter Bank Name: ")

            # Validations
            if len(str(acno)) != 8:
                print("❌ Account Number must be 8 digits")
                return

            if not cname.replace(" ", "").isalpha():
                print("❌ Customer Name should contain only letters")
                return

            if bal <= 0:
                print("❌ Balance must be greater than zero")
                return

            if len(str(pin)) != 4:
                print("❌ PIN must be 4 digits")
                return

            if not bname.replace(" ", "").isalpha():
                print("❌ Bank Name should contain only letters")
                return

            # Safe Insert Query
            iq = "INSERT INTO banking VALUES (%s, %s, %s, %s, %s)"
            cur.execute(iq, (acno, cname, bal, pin, bname))

            con.commit()
            sq = "select * from banking where acno = %s"
            cur.execute(sq, (acno,))
            records = cur.fetchone()
            print(records)
            con.commit()

            print("✅ Data inserted successfully")
            ch = input("Do you want to insert more customer? (Yes/No) ")
            if ch.lower() == "no":
                break

        except mc.DatabaseError as db:
            print("Database Error:", db)

        except ValueError:
            print("❌ Please enter correct numeric values")



# Main Program
# openaccount()
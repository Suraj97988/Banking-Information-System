#BankingProjectDemo.py
import mysql.connector as mc

from BankExcept import DuplicateAccount
# from BankMenu import menu
# from BankDeposit import deposit
# from BankWithDraw import withdraw
# from BankAccountOpen import openaccount
# from BankSearchCustomer import searchcustomer
# from BankCloseAccount import accountclose
# from BankPinGenerateUpdate import pinupdate,pingenerate
# from BankViewCustomers import viewcustomer,viewallcustomers
from AllModules import *
from BankWithDraw import withdraw


def bankinformationsystem():
    while True:
        try:
            menu()
            ch = int(input("Enter your choice: "))
            match ch:
                    case 1:
                        openaccount()
                    case 2:
                        pingenerate()
                    case 3:
                        pinupdate()
                    case 4:
                        try:
                            deposit()
                        except DepositError:
                            print("\tDon't enter -ve/zero for deposit")
                        except ValueError:
                            print("\t Don't enter alnums and sepcial symbols for deposit")
                    case 5:
                        try:
                            withdraw()
                        except WithDrawError as we:
                            print("❌ Withdrawal Error: ",we)
                    case 6:
                        searchcustomer()
                    case 7:
                        viewcustomer()
                    case 8:
                        viewallcustomers()
                    case 9:
                        accountclose()
                    case 10:pass
                        # break
                    case _:
                        print("Please choose a valid choice")
            ch = input("Do you want to continue? (yes/no) ")
            if ch.lower() == "no":
                break
        except ValueError:
            print("Don't Enter alnums and special symbols for choice")

# Main Program

bankinformationsystem()
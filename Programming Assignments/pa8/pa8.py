# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa8
# Date Assigned:    Monday, April 3, 2017
# Date/Time Due:    Saturday, April 8, 2017 -- 11:55pm
#
# Description:      This program asks the user for their balance, an amount of deposits,
#                   and amount of withdraws twice then states the balance of each account.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

class Account:
    def __init__(self, balanceIn, depositIn, withdrawIn):
        self.balance = balanceIn
        self.totalDeposits = depositIn
        self.totalWithdrawals = withdrawIn

    def GetBalance(self):
        return self.balance

def main():
    print()
    print("Enter the following for the first account:")
    a,b,c = eval(input("Beginning balance, total deposit amounts and total withdrawal amounts: "))
    myAcct= Account(a,b,c)

    print()
    print("Enter the following for the second account:")
    a,b,c = eval(input("Beginning balance, total deposit amounts and total withdrawal amounts: "))
    yourAcct = Account(a,b,c)

    print()
    print("First account balance:  $", myAcct.GetBalance())
    print("Second account balance: $", yourAcct.GetBalance())

main()

    

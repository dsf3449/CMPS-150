# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa8x
# Date Assigned:    Monday, April 10, 2017
# Date/Time Due:    Tuesday, April 25, 2017 -- 11:55pm
#
# Description:      This program processes bank transactions using classes/objects.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

class Account:
    def __init__(self, acctNumIn, balanceIn):
        self.__acctNum = acctNumIn
        self.__balance = balanceIn
        self.__totalDeposits = 0
        self.__totalWithdrawals = 0

    def getAcctNum(self):
        return self.__acctNum
    
    def getBalance(self):
        return self.__balance

    def getTotalDeposits(self):
        return self.__totalDeposits

    def getTotalWithdrawals(self):
        return self.__totalWithdrawals

    def deposit(self, amount):
        self.__balance += amount
        self.__totalDeposits += amount
        print(format(self.__acctNum, '14s'), "Deposit", format(amount, '15.2f'), format(self.__balance, '13.2f'))

    def withdrawal(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__totalWithdrawals += amount
            print(format(self.__acctNum, '14s'), "Withdrawal", format(amount, '12.2f'), format(self.__balance, '13.2f'))
        else:
            print(format(self.__acctNum, '14s'), "Withdrawal", format(amount, '12.2f'), format("<denied>", '>13s'))

    def balance(self):
        print(format(self.__acctNum, '14s'), "Balance", format(self.__balance, '29.2f'))

def main():
    #filename = input("What is the name of your input file? ")
    #infile = open(filename, 'r')
    infile = open("trans.py", 'r')
    print()
    
    ID1 = "ABC123" #input("Enter bank account ID #1: ")
    balance1 = 200 #eval(input("Enter balance for bank account #1: "))
    acct1 = Account(ID1, balance1)
    print()
    
    ID2 = "DEF456" #input("Enter bank account ID #2: ")
    balance2 = 500 #eval(input("Enter balance for bank account #2: "))
    acct2 = Account(ID2, balance2)
    print()

    line = infile.readline().strip()

    print("Acct          Trans Type        Amount       Balance")
    print("----------------------------------------------------")

    while line != "X":
        if line == ID1:
            use = acct1
        elif line == ID2:
            use = acct2

        line = infile.readline().strip()

        if line == "D":
            use.deposit(eval(infile.readline()))
        elif line == "W":
            use.withdrawal(eval(infile.readline()))
        elif line == "B":
            use.balance()
            infile.readline()

        line = infile.readline().strip()

    print("----------------------------------------------------")
    print()
    print(acct1.getAcctNum(), "Deposits:", format(acct1.getTotalDeposits(), '19.2f'))
    print(acct1.getAcctNum(), "Withdrawals:", format(acct1.getTotalWithdrawals(), '16.2f'))
    print(acct1.getAcctNum(), "Ending Balance:", format(acct1.getBalance(), '13.2f'))

    print()
    print(acct2.getAcctNum(), "Deposits:", format(acct2.getTotalDeposits(), '19.2f'))
    print(acct2.getAcctNum(), "Withdrawals:", format(acct2.getTotalWithdrawals(), '16.2f'))
    print(acct2.getAcctNum(), "Ending Balance:", format(acct2.getBalance(), '13.2f'))

main()
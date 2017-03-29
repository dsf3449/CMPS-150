# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002

def process(type, previousBalance, changer):
    if type == 'W':
        newBalance = (previousBalance - changer), "Withdrawal"
        if newBalance[0] < 0:
            return "NEC Exception"
        elif newBalance[0] > 0:
            return newBalance
    elif type == 'D':
        newBalance = (previousBalance + changer), "Deposit"
        return newBalance
    elif type == 'B':
        newBalance = previousBalance, "Balance"
        return newBalance
    elif type == 'X':
        print()
    else:
        print()






def main():

    print()
    balance = eval(input("Enter beginning balance: "))
    print()

    infile = open("lab10.data","r")

    # priming read to get first set of data from the file
    trans = infile.readline().strip()
    amount = eval(infile.readline())
    

    while (trans != 'X'):
        # process data just read from the file
        balance = process(trans, balance, amount)
        print(balance[1], balance[0])
        balance = balance[0]
        # get next set of data from the file
        trans = infile.readline().strip()
        amount = eval(infile.readline())
main()
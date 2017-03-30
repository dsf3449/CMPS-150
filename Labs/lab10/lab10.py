# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002

def process(type, previousBalance, changer):
    if type == 'W':
        newBalance = (previousBalance - changer)
        if newBalance < 0:
            print(format("Withdrawal", '15s'), format(changer, '0.2f'), format("Insufficient Funds", '>23s'))
            return previousBalance
        elif newBalance > 0:
            print(format("Withdrawal", '15s'), format(changer, '0.2f'), format(newBalance, '11.2f'))
            return newBalance
    elif type == 'D':
        newBalance = (previousBalance + changer)
        print(format("Deposit", '15s'), format(changer, '0.2f'), format(newBalance, '11.2f'))
        return newBalance
    elif type == 'B':
        newBalance = previousBalance
        print(format("Balance", '26s'), format(newBalance, '0.2f'))
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
        # get next set of data from the file
        trans = infile.readline().strip()
        amount = eval(infile.readline())
main()
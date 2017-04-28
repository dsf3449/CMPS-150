# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa9
# Date Assigned:    Wednesday, April 26, 2017
# Date/Time Due:    Friday, April 28, 2017 -- 11:55pm
#
# Description:      Create a list of valid accts from one file & verify from a second.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

def main():
    infile = open("validAccts.py",'r')
    validAccts = []
    acctNum = infile.readline().strip()
    while acctNum != 'X':
        validAccts.append(acctNum)
        acctNum = infile.readline().strip()
    infile.close()
    print(validAccts)
    print()
    filename = input("Enter the name of input file: ")
    print()
    infile = open(filename, 'r')
    acctNum = infile.readline().strip()
    print("Account   Verification")
    print("----------------------")
    while acctNum != 'X':
        if acctNum in validAccts:
            print(acctNum, "   Valid")
        else:
            print(acctNum, "   Invalid")
        acctNum = infile.readline().strip()

main()

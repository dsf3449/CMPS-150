# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa2
# Date Assigned:    Wednesday, February 1, 2017
# Date/Time Due:    Tuesday, February 7, 2017 -- 11:55pm
#
# Description:      This program uses string and numeric input.
#                   It also processes using arithmetic operators and formatted output.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

def line():
    print("----------------------------------")

# Ask for shares purchased
sharesBought = eval(input("Enter number of shares purchased: "))

# Ask for price per share
pricePerPurchase = eval(input("Enter cost per purchased share: "))

# Ask for shares sold
sharesSold = eval(input("Enter number of shares sold: "))

# Ask for price per share
pricePerSell = eval(input("Enter cost per sold share: "))

# Calculate net gain
netGain = pricePerSell - pricePerPurchase

line()
print("Shares       Price       Total")
line()
print(sharesBought, "       ", format(pricePerPurchase, '0.2f'), "       ", format(sharesBought * pricePerPurchase, '0.2f'))
print(sharesSold, "        ", format(pricePerSell, '0.2f'), "       ", format(sharesSold * pricePerSell, '0.2f'))
print("For the", sharesSold, "shares you sold, your net gain is", format(netGain, '0.2f'), "per share for a total of $", format(sharesSold * netGain, '0.2f'))
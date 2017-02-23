# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa4
# Date Assigned:    Monday, February 20, 2017
# Date/Time Due:    Friday, March 3, 2017 -- 11:55pm
#
# Description:      This program will ask the user for their package type and weight
#                   and computes the price for shipping and the item.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

# Declare loop controller
originalUSD = ''

# Declare static conversion factors
peso = 15.69
pound = 0.8
euro = 0.94
rupee = 66.92
yen = 113.12

# Menu loop
while originalUSD != 0:
    # Get amount of money to convert from the user
    originalUSD = eval(input("Enter the amount of USD to convert (<= 0 to exit): "))

    # Inform the user of their possible choices
    print("Choose currency to convert to:")
    print("1. Argentine Peso")
    print("2. British Pound")
    print("3. European Euro")
    print("4. Indian Rupee")
    print("5. Japanese Yen")
    print("6. Other")

    # Ask the user for their choice
    selection = eval(input("Enter currency selection: "))

    # "Math it" then print the answer

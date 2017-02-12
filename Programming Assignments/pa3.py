# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa3
# Date Assigned:    Friday, February 10, 2017
# Date/Time Due:    Thursday, February 16, 2017 -- 11:55pm
#
# Description:      This program will ask the user for their package type and weight
#                   and computes the price for shipping and the item.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

# For exiting the program under an error condition
import sys

# Function because I'm lazy
def line():
    print("----------------------------------")

# Declare statics
itemPerish = 5.95
itemNonPerish = 1.95
itemPerishTax = itemPerish * .085
itemNonPerishTax = itemNonPerish * .085

# Explain the selection options
print("Enter package type.  'N' = non-perishable; 'P' = perishable")

# Ask the user for their answer
packageType = input("What type of package? ")

# Ask the user for the weight of the package
packageWeight = eval(input("What is the weight of your package? "))


if packageType == "N":
    # The user chose a non-perishable package
    if packageWeight > 0 and packageWeight <= 2:
        # The package weighs between 0-2 lbs
        shippingCost = 1.95
    elif packageWeight > 2 and packageWeight <= 5:
        # The package weighs between 2-5 lbs
        shippingCost = 3.95
    elif packageWeight > 5 and packageWeight <= 8:
        # The package weighs between 5-8 lbs
        shippingCost = 7.95
    elif packageWeight > 8:
        # The package weighs over 8 lbs
        shippingCost = 9.95
    else:
        # Invalid input, throw error
        line()
        print("Error: Invalid package weight")
        line()
        # Exit the program to prevent invalid printing
        sys.exit()
    
    # Print output for type non-perishable
    print("Item Cost                ", itemNonPerish, "(non-perishable)")
    print("Tax (8.5%)               ", format(itemNonPerishTax, '1.2f'))
    print("Total Cost               ", format(itemNonPerish + itemNonPerishTax, '1.2f'))
    line()
    print("Package Weight:", packageWeight, "pounds")
    print("Shipping Cost            ", shippingCost)
    line()
    print("Total (incl. shipping)   ", format(itemNonPerish + itemNonPerishTax + shippingCost, '1.2f'))

elif packageType == "P":
    # The user chose a perishable package
    if packageWeight > 0 and packageWeight <= 2:
        # The package weighs between 0-2 lbs
        shippingCost = 2.95
    elif packageWeight > 2 and packageWeight <= 5:
        # The package weighs between 2-5 lbs
        shippingCost = 5.95
    elif packageWeight > 5 and packageWeight <= 8:
        # The package weighs between 5-8 lbs
        shippingCost = 9.95
    elif packageWeight > 8:
        # The package weighs over 8 lbs
        shippingCost = 19.95
    else:
        # Invalid input, throw error
        line()
        print("Error: Invalid package weight")
        line()
        # Exit the program to prevent invalid printing
        sys.exit()
    
    # Print output for type perishable
    print("Item Cost                ", itemPerish, "(perishable)")
    print("Tax (8.5%)               ", format(itemPerishTax, '1.2f'))
    print("Total Cost               ", format(itemPerish + itemPerishTax, '1.2f'))
    line()
    print("Package Weight:", packageWeight, "pounds")
    print("Shipping Cost            ", shippingCost)
    line()
    print("Total (incl. shipping)   ", format(itemPerish + itemPerishTax + shippingCost, '1.2f'))

else:
    # Invalid package type, throw error
    line()
    print("Error: Unknown package type.")
    line()
    # Exit the program
    sys.exit()
# Author:       David Fontenot  
# CLID/Section: dsf3449/C00177513/Section 002 
# Lab #6

# Task #1:  Odd and Even Numbers
# get first input item
number = eval(input("Enter a number (0 or less to exit): "))

# repeat loop based on input item NOT being the sentinel value
while number > 0:
    # process data - determine if input data is odd or even
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
    # get next input item
    number = eval(input("Enter a number (0 or less to exit): "))

# print a blank line before moving on to task #2
print()

# Task #2:  Print pounds/kilograms table
print("Pounds     Kilograms")
print("--------------------")

count = 5

while count < 101:
    kilograms = 0.453592 * count
    print(format(count,'5.0f'),format(kilograms,'12.2f'))
    count = count + 5
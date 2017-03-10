# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa5
# Date Assigned:    Monday, March 6, 2017
# Date/Time Due:    Friday, March 10, 2017 -- 11:55pm
#
# Description:      This program reads the data from a file 'pa5data.py', stops when reaching 0,
#                   and gathers various statistics from the data.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

# Import sys for error handling
import sys

# Declare vars
positive = 0
negative = 0
even = 0
odd = 0
sum = 0
count = 0
average = 0

# Open the file for reading
file = open("pa5data.py", 'r')

# Confirm that the file is not blank.
try:
    currentValue = eval(file.readline())
except SyntaxError:
    sys.exit("Your file is blank!")

while currentValue != 0:
    if currentValue > 0:
        positive = positive + 1
    elif currentValue < 0:
        negative = negative + 1

    if currentValue % 2 == 0:
        even = even + 1
    elif currentValue % 2 != 0:
        odd = odd + 1
    else:
        # This should never happen
        print("Number is neither odd or even.")
    
    # Sum the current number
    sum = sum + currentValue

    # Increment counter
    count = count + 1

    # Read the next number in the file
    currentValue = eval(file.readline())

# The file is no longer required, close it.
file.close()

# Loop is done, begin printing
print("Positive =", positive)
print("Negative =", negative)
print("Even =", even)
print("Odd =", odd)
print("Sum =", sum)
print("Count =", count)
print("Average =", format(sum/count, '0.2f'))
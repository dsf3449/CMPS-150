# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa1
# Date Assigned:    Tuesday, January 24, 2017
# Date/Time Due:    Friday, January 27, 2017 -- 11:55pm
#
# Description:      This program uses string and numeric input.
#                   It also processes using arithmetic operators.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

# ask the user for their name using an input statement
username = input("Enter your name: ")
# ask the user for two(2) numbers using eval input
hoursWorked = eval(input("How many hours did you work? "))
hourlyRate = eval(input("What is your hourly rate? "))

# multiply the hours and hourly rate to get gross pay
grossPay = hoursWorked * hourlyRate
# multiply the gross pay times 15 percent to get federal tax deduction
fedDeduction = grossPay * .15
# multiply the gross pay times 4 percent to get state tax deduction
stateDeduction = grossPay * .04
# subtract federal tax deduction and state tax deduction from gross pay to get net pay
netPay = grossPay - fedDeduction - stateDeduction

# print output similar to the sample run
print()
print("Payroll Report for", username)
print("---------------------------------")
print("Gross Pay:  ", grossPay)
print("Federal Tax:", fedDeduction)
print("State Tax:  ", stateDeduction)
print("Net Pay:    ", netPay)
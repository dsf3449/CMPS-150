# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa6
# Date Assigned:    Tuesday, March 14, 2017
# Date/Time Due:    Saturday, March 18, 2017 -- 11:55pm
#
# Description:      This program reads the data from a file 'pa6numbers.py', stops when reaching -1,
#                   and presents the data in a table format.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

# Open the file for reading
file = open("pa6numbers.py", 'r')

# Initilize variables
maxInf = 0
minSen = 10000
maxInfCity = ''
minSenCity = ''

# Print the top of the table
print(format("City/State", '17s'), format("Pneumonia Rate", '16s'), format("Infant Rate", '15s'), "Senior Rate")
print("--------------------------------------------------------------")

while True:
    # Get the city / state, needs strip for newline char
    line = file.readline().strip()
    
    # Read all the numerical values and evaluate them
    all = eval(file.readline())
    pnu = eval(file.readline())
    inf = eval(file.readline())
    sen = eval(file.readline())
    
    # Exit the loop if we reach the sentinal value
    if all == -1:
        break
    
    # Do math to get the percentages
    pnuRate = (pnu/all) * 100
    infRate = (inf/all) * 100
    senRate = (sen/all) * 100
    
    # Print the line!
    print(format(line, '20s'), format(pnuRate, '7.4f'), format(infRate, '15.4f'), format(senRate, '15.4f'))
    
    # Determine if the infant rate of the current city is greater than the previous city
    if infRate > maxInf:
        # If so, assign that value to the max variable
        maxInf = infRate
        maxInfCity = line

    # Same as above, just if the senior rate is less than the previous city
    if senRate < minSen:
        minSen = senRate
        minSenCity = line

# Print the maximum infant rate
print()
print("Maximum Infant Rate")
print("------------------------")
print(format(maxInfCity, '17s'), format(maxInf, '0.4f'))

# Print the minimum senior rate
print()
print("Minimum Senior Rate")
print("------------------------")
print(format(minSenCity, '16s'), format(minSen, '0.4f'))
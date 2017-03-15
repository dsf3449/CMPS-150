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

file = open("pa6numbers.py", 'r')

all = ''
maxInf = 0
minSen = 0
maxInfCity = ''
minSenCity = ''

print(format("City/State", '17s'), format("Pneumonia Rate", '16s'), format("Infant Rate", '15s'), "Senior Rate")
print("--------------------------------------------------------------")

while all != -1:
    # Get the city / state, needs strip for newline char
    line = file.readline().strip()

    all = eval(file.readline())
    pnu = eval(file.readline())
    inf = eval(file.readline())
    sen = eval(file.readline())
    pnuRate = (pnu/all) * 100
    infRate = (inf/all) * 100
    senRate = (sen/all) * 100
    minSen = senRate
    print(format(line, '20s'), format(pnuRate, '7.4f'), format(infRate, '15.4f'), format(senRate, '15.4f'))

    if infRate > maxInf:
        maxInf = infRate
        maxInfCity = line

    if senRate < minSen:
        minSen = senRate
        minSenCity = line

print("Maximum Infant Rate")
print("--------------------")
print(format(maxInfCity, '20s'), format(maxInf, '0.4f'))

print("Minimum Senior Rate")
print("--------------------")
print(format(minSenCity, '20s'), format(minSen, '0.4f'))
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

print(format("City/State", '17s'), format("Pneumonia Rate", '16s'), format("Infant Rate", '15s'), "Senior Rate")
print("--------------------------------------------------------------")

while all != -1:
    # Get the city / state, needs strip for newline char
    line = file.readline().strip()

    all = eval(file.readline())
    pnu = eval(file.readline())
    inf = eval(file.readline())
    sen = eval(file.readline())
    print(format(line, '20s'), format((pnu/all) * 100, '7.4f'), format((inf/all) * 100, '15.4f'), format((sen/all) * 100, '15.4f'))
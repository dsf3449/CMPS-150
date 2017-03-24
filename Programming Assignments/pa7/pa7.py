# Author:           David Fontenot
# CLID/ULID:        dsf3449/C00177513
# Course/Section:   CMPS 150 - Lecture Section #002
# Assignment:       pa7
# Date Assigned:    Wednesday, March 22, 2017
# Date/Time Due:    Tuesday, March 28, 2017 -- 11:55pm
#
# Description:      This program will show the user a menu of choices, then calls a function
#                   to do whatever math the user requests from the menu.
#
# Certificate of Authenticity:
# I certify that this assignment is entirely my own work.

import math

def slope():
    # Value returning function requirement satisfied
    var1 = eval(input("Enter coordinate #1: "))
    var2 = eval(input("Enter coordinate #2: "))
    numerator = var2[1] - var1[1]
    denominator = var2[0] - var1[0]
    return numerator/denominator

def triType():
    # Void function requirement satisfied
    var1 = eval(input("Enter the sides of the triangle: "))
    if var1[0] == var1[1] and var1[0] == var1[2]:
        print("This is an equilateral triangle.")
    elif var1[0] == var1[1] or var1[0] == var1[2]:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")

def quadrant():
    var1 = eval(input("Enter coordinate: "))
    if var1[0] > 0 and var1[1] > 0:
        print("This point is in Quadrant I.")
    elif var1[0] < 0 and var1[1] > 0:
        print("This point is in Quadrant II.")
    elif var1[0] < 0 and var1[1] < 0:
        print("This point is in Quadrant III.")
    elif var1[0] > 0 and var1[1] < 0:
        print("This point is in Quadrant IV.")
    elif var1[0] == 0 and var1[1] == 0:
        print("This point is the origin.")
    elif var1[0] == 0 and var1[1] != 0:
        print("This point is on the y-axis.")
    elif var1[0] != 0 and var1[1] == 0:
        print("This point is on the x-axis.")
    else:
        print("Error.")

def roots():
    var1 = eval(input("Enter 3 coefficients: "))
    root1 = ((var1[1] * -1) + math.sqrt((var1[1] ** 2) - (4 * var1[0] * var1[2]))) / (2 * var1[0])
    root2 = ((var1[1] * -1) - math.sqrt((var1[1] ** 2) - (4 * var1[0] * var1[2]))) / (2 * var1[0])
    if root1.is_integer() == False or root2.is_integer() == False:
        print("Roots are: ", format(root1, '0.2f'), ", ", format(root2, '0.2f'), sep="")
    else:
        print("Roots are: ", format(root1, '0.0f'), ", ", format(root2, '0.0f'), sep="")

def main():
    selection = 0
    while selection != 5:
        print("1) Compute Slope of a Line")
        print("2) Determine Triangle Type")
        print("3) Determine Quadrant")
        print("4) Compute Roots of Quad Eq")
        print("5) Quit")
        
        selection = eval(input("Enter Selection: "))
        
        if selection == 1:
            print("Slope = ", format(slope(), '0.2f'))
        elif selection == 2:
            triType()
        elif selection == 3:
            quadrant()
        elif selection == 4:
            roots()

main()
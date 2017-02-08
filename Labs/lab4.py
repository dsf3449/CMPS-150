# Author:       David Fontenot  
# CLID/Section: dsf3449/C00177513/Section 002 
# Lab #4 

# Ask the user to enter the lengths of three sides of a triangle
side1,side2,side3 = eval(input("Enter the triangle sides: "))


# Check for "valid" lengths ...
# if valid -- compute perimeter -- else print "invalid"

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Perimeter =", side1 + side2 + side3)
else:
    print("One of your sides in invalid.")
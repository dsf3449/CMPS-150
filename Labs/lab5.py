# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
# Lab #5


# ask the user to enter an x,y coordinate
coords = eval(input("Enter a coordinate pair (separated by a comma): "))


# check for the origin, x-axis OR y-axis & all 4 quadrants
if coords[0] == 0 and coords[1] == 0:
    print("This point is the origin.")
elif coords[0] == 0 or coords[1] == 0:
    print("This point is on an axis.")
elif coords[0] > 0 and coords[1] > 0:
    print("This point is in Quadrant I.")
elif coords[0] < 0 and coords[1] > 0:
    print("This point is in Quadrant II.")
elif coords[0] < 0 and coords[1] < 0:
    print("This point is in Quadrant III.")
elif coords[0] > 0 and coords[1] < 0:
    print("This point is in Quadrant IV.")
else:
    print("Invalid input.")
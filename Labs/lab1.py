# Author: David Fontenot
# CLID/Section: C00177513/002

# get user input
state = input("Enter a state abbrevation: ")
length = eval(input("Enter the approximate length of this room: "))
width = eval(input("Enter the approximate width of this room: "))

# compute age in days
area = length * width

# print output
print()
print("The state you entered is:", state)
print("The area of this room is", area, "square feet!")

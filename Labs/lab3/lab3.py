# lab3.py

# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
 
import math 
# print a couple of blank lines before the program begins
print()
print()

# asking for input
# ask the user for the radius of the pizza (in inches)
radius = eval(input("Enter radius of pizza: "))
# compute the area of the pizza (in square inches) 
pizzaArea = math.pi * radius * radius

# ask the user for the price of the pizza
price = eval(input("Enter price of pizza: "))
# compute the price of the pizza per square inch 
ppsi = price / pizzaArea

# print out the price of the pizza per square inch 
print("Price per square inch: $", format(ppsi, '0.2f'))

# print a couple of blank lines before the next section of code begins
# asking for input 
print()

# ask the user to enter a 3-letter word
# you are allowed only ONE input statement

word = input("Enter a 3-letter word: ")

# print the ASCII code (a number) for each letter of the word just input
print(word[0], " = ", ord(word[0]))
print(word[1], " = ", ord(word[1]))
print(word[2], " = ", ord(word[2]))


# print a couple of blank lines when the program is done
print()
print()

# Author:            David Fontenot
# CLID/ULID/Section: dsf3449/C00177513 Section 002 
# Part I of this lab will use the math library, which means
# it must be imported

import math

# Print sin/cos/tan for the "common" angles of 30, 45 & 90 degrees
# Remember, sometimes one of these trig functions is undefined 
print()
print("Angle         Sine       Cosine     Tangent")
print("-------------------------------------------") 

# convert degrees to radians
degree1 = 30
radian1 = math.pi / 180 * degree1
degree2 = 45
radian2 = math.pi / 180 * degree2
degree3 = 90
radian3 = math.pi / 180 * degree3

# there are NO errors in the following PRETTY print statements

print("{0:6}  {1:10.3f}  {2:10.3f}  {3:10.3f}"
     .format(degree1,math.sin(radian1),math.cos(radian1),math.tan(radian1)))
print("{0:6}  {1:10.3f}  {2:10.3f}  {3:10.3f}"
     .format(degree2,math.sin(radian2),math.cos(radian2),math.tan(radian2)))
print("{0:6}  {1:10.3f}  {2:10.3f}  {3:10.3f}"
     .format(degree3,math.sin(radian3),math.cos(radian3),math.tan(radian3))) 

# Print 2 blank lines
print()
print()

# Part II of this lab is simply using input statements and
# arithmetic expressions 
# Ask the user to input hours and hourly rate, then compute gross pay
# First, complete the following input statements 
hours = eval(input("Input your hours: "))
rate = eval(input("Input your pay rate: "))

# Write an equation to compute gross pay using the variables above 
grossPay = hours * rate

# Print 1 blank line
print()

# Print out hours, rate and gross pay that you just computed 
print("Hours =", hours)
print("Rate =", rate)
print("Gross pay =", grossPay)
 

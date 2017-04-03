# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
# lab9.py 

# Import the math function for pi in calculations
import math

# Define all the math functions required by the program
def AC(radius):
    area = math.pi * radius ** 2
    return area 

def AR(length, width):
    area = length * width
    return area

def VC(radius, height):
    area = math.pi * height * radius ** 2
    return area

def VR(length, width, height):
    area = length * width * height
    return area

def VS(radius):
    area = (4/3) * math.pi * radius ** 3
    return area

def SAC(length):
    area = 6 * length ** 2
    return area

def SAS(radius):
    area = 4 * math.pi * radius ** 2
    return area

def main():
    # Open the file
    infile = open("lab9.input","r")
    
    # Read the file, strip the newline char
    type = (infile.readline()).strip()
    
    # While we haven't reached the sentinal value...
    while type != "###":
        # Area of a circle
        if type == "AC":
            radius = eval(infile.readline())
            print(format("Area of a Circle","30s"),format(AC(radius),"15.2f"))
        
        # Area of a rectangle
        elif type == "AR":
            length = eval(infile.readline())
            width = eval(infile.readline())
            print(format("Area of a Rectangle/Square","30s"),format(AR(length, width),"15.2f"))
        
        # Volume of a cylinder
        elif type == "VC":
            radius = eval(infile.readline())
            height = eval(infile.readline())
            print(format("Volume of a Cylinder","30s"),format(VC(radius, height),"15.2f"))
        
        # Volume of a rectangular prism
        elif type == "VR":
            length = eval(infile.readline())
            width = eval(infile.readline())
            height = eval(infile.readline())
            print(format("Volume of a Rectangular Prism","30s"),format(VR(length, width, height),"15.2f"))
        
        # Volume of a sphere
        elif type == "VS":
            radius = eval(infile.readline())
            print(format("Volume of a Sphere","30s"),format(VS(radius),"15.2f"))
        
        # Surface area of a cube
        elif type == "SAC":
            length = eval(infile.readline())
            print(format("Surface Area of a Cube","30s"),format(SAC(length),"15.2f"))
        
        # Surface area of a sphere
        elif type == "SAS":
            radius = eval(infile.readline())
            print(format("Surface Area of a Sphere","30s"),format(SAS(radius),"15.2f"))
        
        # Unknown type??
        else:
            print("Invalid type supplied..")
        
        # Get the next type for the loop
        type = (infile.readline()).strip()

    # File isn't needed anymore
    infile.close()

# Call the main fucntion
main()
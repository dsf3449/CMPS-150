# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
# Lab #7
 
inFile = open("lab7.fuel")
    
print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")  

count = 0

# this is a count-controlled loop
for i in range(0, 15):
    # read and process data
    fuelType = inFile.readline().strip()
    fuelAmount = eval(inFile.readline())

    if fuelType == 'S':
        word = "Super Unleaded"
        bill = fuelAmount * 2.62
    elif fuelType == 'P':
        word = "Unleaded Plus"
        bill = fuelAmount * 2.36
    elif fuelType == 'R':
        word = "Regular Unleaded"
        bill = fuelAmount * 2.12
    elif fuelType == 'D':
        word = "Diesel"
        bill = fuelAmount * 2.35

    gallons = fuelAmount
    # print each line of output
    print(format(word,'20s'),format(gallons,'7.2f'),format(bill,'8.2f'))  


inFile.close()

# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
# Lab #7

# Open the file
inFile = open("lab7.fuel")

# Print the top of the chart
print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")  

# We want the program to read 15, exactly.
for i in range(0, 15):
    # Read the data from the file
    fuelType = inFile.readline().strip()
    fuelAmount = eval(inFile.readline())

    # Assign the full fuel type based on the fuelType read from the file
    # then calculate the bill based on the cost for that fuelType.
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

    # Assign fuelAmount to gallons for printing
    gallons = fuelAmount
    
    # Print each line of output
    print(format(word,'20s'),format(gallons,'7.2f'),format(bill,'8.2f'))  

# Close the file to free memory
inFile.close()

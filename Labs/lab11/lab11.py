# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/002
# Lab #11

import random

class Car:
    def __init__(self, symbolIn):
        self.location = 0
        self.symbol = symbolIn
        
    def MoveCar(self):
        self.location = self.location + random.randint(1,5)  

    def DisplayCar(self):
        if (self.location > 0):
            for i in range(self.location):
                print('*',end="")
            print(self.symbol)
        else:
            print(self.symbol)
    
    def GetLocation(self):
        return self.location

    def GetSymbol(self):
        return self.symbol
    
def main():
    #  This main function will create two cars 
    #  Then it will “race” them by moving them 5 times 

    myCar = Car("Nona")
    myCar2 = Car("George")
    
    for i in range(5):
        # move and display the first car created
        myCar.MoveCar()
        myCar.DisplayCar()
        myCar2.MoveCar()
        myCar2.DisplayCar()
        print()
    
    # determine which car “moved” farthest (location data member is larger)
    # and declare/print that is the “winner”
    if myCar.GetLocation() > myCar2.GetLocation():
        print(myCar.GetSymbol(), "wins!")
    elif myCar.GetLocation() < myCar2.GetLocation():
        print(myCar2.GetSymbol(), "wins!")
    elif myCar.GetLocation() == myCar2.GetLocation():
        print("Tie!")

main()
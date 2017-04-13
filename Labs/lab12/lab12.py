#  Author:        David Fontenot
#  CLID/Section:  dsf3449/C00177513/002
#  lab12.py 

class Clock:
    def __init__(self, hrsIn, minsIn, secsIn):
        self.hours = hrsIn
        self.minutes = minsIn
        self.seconds = secsIn


    def SetTime(self, newHrsIn, newMinsIn, newSecsIn):
        # write this class method
        self.hours = newHrsIn
        self.minutes = newMinsIn
        self.seconds = newSecsIn

    def GetHours(self):
        return self.hours

    def GetMinutes(self):
        # write this class method
        return self.minutes

    def GetSeconds(self):
        # write this class method
        return self.seconds

    def DisplayTime24(self):
        if (self.hours >= 24):
            self.hours = self.hours - 24
        print("The time is ", self.hours, ": ",end="", sep="")
        if (self.minutes < 10):
            print("0", self.minutes, ": ", end="", sep="")
            # finish the rest of this class method
        elif (self.minutes >= 10):
            print(self.minutes, ": ", end="", sep="")
        if (self.seconds < 10):
            print("0", self.seconds, sep="")
        elif (self.seconds >= 10):
            print(self.seconds, sep="")

    def DisplayTime12(self):
        if (self.hours >= 24):
            self.hours = self.hours - 24
        print("The time is ",end="", sep="")
        if (self.hours <= 11 and self.hours != 0):
            # finish the rest of this class method
            print(self.hours, ": ", end="", sep="")
            ender = "AM"
        elif (self.hours == 0):
            print("12: ", end="", sep="")
            ender = "AM"
        elif (self.hours == 12):
            print("12: ", end="", sep="")
            ender = "PM"
        elif (self.hours >= 13):
            print((self.hours - 12), ": ", end="", sep="")
            ender = "PM"
        if (self.minutes < 10):
            print("0", self.minutes, ": ", end="", sep="")
        elif (self.minutes >= 10):
            print(self.minutes, ": ", end="", sep="")
        if (self.seconds < 10):
            print("0", self.seconds, " ", ender, sep="")
        elif (self.seconds >= 10):
            print(self.seconds, " ", ender, sep="")

    def IncrementClock(self):
        self.seconds = self.seconds + 1
        if (self.seconds == 60):
            self.seconds = 0
            self.minutes = self.minutes + 1
            # finish the rest of this class method
        if (self.minutes == 60):
            self.minutes = 0
            self.hours = self.hours + 1

def main():
    myClock = Clock(24,0,0)     # create a clock with a time of midnight
    myClock.DisplayTime12()     # display it with a 12-hour format
    myClock.DisplayTime24()     # display it with a 24-hour format
    print()

    myClock.SetTime(22,30,5)    # change the time to 10:30:05 PM
    myClock.DisplayTime12()     # display it with a 12-hour format
    myClock.DisplayTime24()     # display it with a 24-hour format
    print()

    myClock.SetTime(11,59,59)   # change the time to 11:59:59 AM
    myClock.DisplayTime12()     # display it with a 12-hour format
    myClock.DisplayTime24()     # display it with a 24-hour format
    print()

    myClock.IncrementClock()            # increment the clock (make time pass) by 1 second
    myClock.DisplayTime12()     # display new/current time in 12-hour format
    myClock.DisplayTime24()     # display new/current time in 24-hour format
    print()


main()
# Author:       David Fontenot
# CLID/Section: dsf3449/C00177513/Section 002
# lab8.py 

#****************** LAB Average  ******************
def labAvg(infile): 
    g1 = eval(infile.readline())
    g2 = eval(infile.readline())
    g3 = eval(infile.readline())
    g4 = eval(infile.readline())
    g5 = eval(infile.readline())
    g6 = eval(infile.readline())
    g7 = eval(infile.readline())
    
    print("Lab Grades:", g1, g2, g3, g4, g5, g6, g7)
    
    sum = g1 + g2 + g3 + g4 + g5 + g6 + g7 
    avg = sum / 7    # computes avg (number between 1 & 10)
    avg = avg / 10   # computes % (number between 0 & 1)
    
    return avg

#****************** PA Average  ****************** 
def paAvg(infile):
    g1 = eval(infile.readline())
    g2 = eval(infile.readline())
    g3 = eval(infile.readline())
    
    print("PA Grades:", g1, g2, g3)
    
    sum = g1 + g2 + g3
    avg = sum / 3
    avg = avg / 100
    
    return avg

#****************** EXAM Average  ****************** 
def examAvg(infile):
    g1 = eval(infile.readline())
    print("Exam Grades:", g1)
    
    avg = g1 / 100
    
    return avg

#****************** MAIN/DRIVER  ******************
def main(): 
    # main will call each of your average functions
    # to compute each components of overall class avg
    # call the function to compute your LAB average
    # put the return value in the variable labAverage 
    
    infile = open("lab8.grades",'r')
    labAverage = labAvg(infile) 
    
    # call the function to compute your PA average  
    paAverage = paAvg(infile)
    
    # call the function to computer your EXAM average 
    examAverage = examAvg(infile)
    
    # close the file
    infile.close()
    
    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet 
    overallAverage =  (labAverage * 10) + (paAverage * 15) + (examAverage * 75)
    
    # print results
    print("  Lab Average =",format(labAverage * 100, '0.2f'), "%")
    print("   PA Average =",format(paAverage * 100, '0.2f'), "%")
    print(" Exam Average =",format(examAverage * 100, '0.2f'), "%")
    print("-------------")
    print("Class Average =",format(overallAverage, '0.2f'), "%")

main()
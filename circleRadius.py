#find the area of a circle
# pi * r **2

from math import *
    
def main():
    print(circleArea())

#get the area
def circleArea():
    r = input("What is the circle's radius? ")
    a = pi * float(r)**2
    return(a)

main()
    
    

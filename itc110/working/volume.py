#Calculate volume and surface of a sphere.

from math import*

def main():
    r = int(input("Enter radius of the sphere: "))
    volume = 4/3 * 3.14 * r ** 3
    print("The volume of the shere is ",  volume)

main()

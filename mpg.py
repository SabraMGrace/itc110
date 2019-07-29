#distance.py

def main():
    print("Calculate mpg!")
    print()
    
    #input
    miles = float(input("How many miles are you driving? "))
    gallons = float(input("How many gallons of gas did you use? "))
    ##mpg = miles / gallons
    
    if miles <=0:
        print("You haven't driven anywhere! Miles must be greater than zero. Try again.")
    elif gallons <=0:
        print("Uh oh! You need to get gas! Gallons of gas must be greater than zero.")
    else:
    #calculate and display mpg.
        mpg = round((miles / gallons), 2)
        print("Miles per Gallon:", mpg)

    print("Goodbye!")


main()



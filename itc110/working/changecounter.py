#change counter program

def main():

    print("Enter the count of each coin type to calculate the total change value")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    dollars = int(input("Bills: "))

    totalValue = .25*quarters + .10*dimes + 0.5*nickels + 0.1*pennies + 1.00*dollars
    print()
    print("You have a total of $" + (str)(round(totalValue,2)))
main()
                        

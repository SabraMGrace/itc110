#program to comput the factorial of a number
#illustrates for loop with an accumulator

def main():
    n = int(input("Enter a number to calculate its factorial: "))

    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
        print("factor", factor)
        print

    print("The factorial of ", n, " is", fact)


main()

# Sabra Grace
# ITC110
# Assignment FIb
# 8/12/19

# fibonacciCalculator.py

def main():
    print("This program calculates the nth Fibonacci value, starting with 0, 1, 1, 2, 3...")
    # get input.
    n = int(input("Enter the value of n: "))  
    fibNum = fibCalc(n)
    print("The nth Fibonacci number is " + str(fibNum) + ".")


def fibCalc(n):
    if n <= 0:
        print("Please enter a positive integer.")
    # first Fibonacci number is 0.
    elif n == 1:
        return 0
        print("The first Fibonacci number is 0. Try a larger number next time.")
    # second Fibonacci number is 1.
    elif n == 2:
        return 1
        print("The second Fibonacci number is 1. Try a larger number next time.")
    # third Fibonacci number is 1.
    elif n == 3:
        return 1
        print("The third Fibonacci number is 1. Try a larger number next time.")
    # calculate and display Fibonacci number.
    else:
        return fibCalc(n-1) + fibCalc(n-2)

    

main()

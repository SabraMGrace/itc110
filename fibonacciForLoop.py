# Sabra Grace
# ITC110
# Assignment FIb
# 8/12/19

# fibonacciForLoop.py

def main():
    print("This program calculates the nth Fibonacci value, starting with 0, 1, 1, 2, 3...")
    # get input.
    n = int(input("Enter the value of n: "))

    prev, curr = 1, 1

    for i in range(n-2):
        curr, prev = curr + prev, curr

    print("The nth Fibonacci number is ", curr)

main()

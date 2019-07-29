# tempWarning
# A program to convert Celsius temps to Fahrenheit.
# This version issues heat and cold warnings.

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", (fahrenheit), "degrees Fahrenheit.")
    if fahrenheit >= 90:
        print("It's really hot out there, be careful!")
    if fahrenheit <= 30:
        print ("Brrrrr. be sure to dress warmly!")
    else:
        print ("Enjoy the nice weather today!")

main()

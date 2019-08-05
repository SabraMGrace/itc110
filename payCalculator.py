# Sabra Grace
# itc110
# 8/4/19
# Week 8 Assignment
# payCalculator.py


# Calculate the amount of pay earned last week.
def main():
    print("Weekly Pay Calculator!\n")
    payCalculator()

# get input
def payCalculator():
    hours = float(input("How many hours did you work last week? "))
    wage = float(input("What is your hourly wage? "))

# calculate pay and account for overtime pay
    if hours >= 168:
        print("\n Go home to rest! You have worked WAY too much!")
    if hours <= 40 and hours > 0:
        totalPay = hours * wage
        print("\n You earned a total of ${0:0.2f}".format(totalPay))
    elif hours > 40:
        regPay = 40 * wage
        overtimeHours = hours - 40
        overtimePay = overtimeHours * (wage * 1.5)
        totalPay = overtimePay + regPay
        print("\n You earned a total of ${0:0.2f}".format(totalPay))
    else:
        print("\n You didn't work last week. You haven't earned any wages.")


main()

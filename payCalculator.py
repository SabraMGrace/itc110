# Sabra Grace
# itc110
# 8/4/19
# Week 8 Assignment
# payCalculator.py


# Calculate the amount of pay earned last week.
def main():
    print("Weekly Pay Calculator")
    payCalculator()

# get input
def payCalculator():
    hours = float(input("How many hours did you work last week? "))
    wage = float(input("What is your hourly wage? "))

# calculate pay and account for overtime pay
    if hours > 40:
        regPay = 40 * wage
        overtimeHours = hours - 40
        overtimePay = overtimeHours * (wage * 0.5)
        totalPay = overtimePay + regPay
        print("You earned a total of $", + (totalPay))
    elif hours <= 0:
        print("You didn't work last week. You haven't earned any wages.")
    elif hours > 168:
        print("Are you kidding? You worked every single hour of the day last week? You need to go home and rest!")
    else:
        totalPay = hours * wage
        print("You earned a total of $", + (totalPay))


main()

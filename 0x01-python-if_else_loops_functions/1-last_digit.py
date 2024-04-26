#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit from the absolute value of number
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Conditions to check the last digit and print appropriate messages
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))

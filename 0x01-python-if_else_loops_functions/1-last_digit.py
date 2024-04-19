#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit from the absolute value of number
last_digit = abs(number) % 10

# Conditions to check the last digit and print appropriate messages
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

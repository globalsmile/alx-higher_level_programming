#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = 0
transformed_last_digit = 0
transformed_number = 0
if number < 0:
    transformed_number = (-1 * number)
    last_digit = transformed_number % 10
    transformed_last_digit = (-1 * last_digit)
    if transformed_last_digit == 0:
        print(f"{str} {number} is {transformed_last_digit} and is 0")
    else:
        print(f"{str} {number} is {transformed_last_digit} and is less than 6"
              f" and not 0")
else:
    last_digit = number % 10
    if last_digit == 0:
        print(f"{str} {number} is {last_digit} and is 0")
    elif last_digit < 6:
        print(f"{str} {number} is {last_digit} and is less than 6 and not 0")
    else:
        print(f"{str} {number} is {last_digit} and is greater than 5")

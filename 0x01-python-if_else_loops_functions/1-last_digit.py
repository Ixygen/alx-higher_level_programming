#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    compare = print('greater than 5')
elif last_digit == 0:
    compare = print('is zero')
else:
    compare = print('less than 6 and not 0')
print(f"Last digit of {number} is {last_digit) and {compare}")

#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # generates a random integer between -10000 and 10000, inclusive

print("Last digit of", number, "is", abs(number) % 10, end=" ")

if abs(number) % 10 > 5:
    print("and is greater than 5")
elif abs(number) % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

print()  # prints a newline character

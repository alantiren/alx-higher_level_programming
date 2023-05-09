#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # generates a random integer between -10 and 10, inclusive

print(number)

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
    
print()  # prints a newline character

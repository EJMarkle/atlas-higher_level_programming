#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = abs(number) % 10
if lastDig == 0:
    print(f"The last digit of {number} is 0 and is 0")
elif lastDig > 5:
    print(f"The last digit of {number} is {lastDig} and is greater than 5.")
elif lastDig < 6 and not 0:
    print(f"The last digit of {number} is {lastDig} and is less than 6 and not 0.")

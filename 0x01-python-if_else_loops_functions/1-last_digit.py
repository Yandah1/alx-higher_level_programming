#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
result = abs(number) % 10

print("Last digit of {} is {} ".format(number, result), end="")

if result > 5:
    print("and is greater than 5")
elif result == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
result = n % 10

if number > 0:
    print("Last digit of {} is {} and is".format(number, result), end="")
if result > 5:
    print("and is greater than 5")
elif result == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")


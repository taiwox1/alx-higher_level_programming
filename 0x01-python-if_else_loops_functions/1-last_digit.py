#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ln = number
n = number
if number < 0:
    ln = (-1) * n
for i in range(5):
    ln = ln % 10
if (n < 0):
    ln = -ln
if ln > 5:
    print("Last digit of {:0} is {:1} and is greater than 5".format(n, ln))
elif ln == 0:
    print("Last digit of {:0} is {:1} ".format(n, ln), end="")
    print("and is zero")
elif ln < 6 and ln != 0:
    print("Last digit of {} is {:1} ".format(n, ln), end="")
    print("and is less than 6 and not 0")

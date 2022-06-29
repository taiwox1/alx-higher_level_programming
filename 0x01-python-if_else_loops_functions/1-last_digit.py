#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(number)
if number < 0:
    num = (-1) * number
else:
    num = number

for i in range(5):
    if (num > 10):
        num = num % 10
        print(num)
print(num)
if num > 5:
    print("Last digit of {:0} is {:1} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {:0} is {:1} and is zero".format(number, num))
elif num < 6 and num != 0:
   print("Last digit of {:0} is {:1} and is less than 6 and not 0".format(number, num))

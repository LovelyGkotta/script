import random
import time
print("enter a number range(1,x)")
rangeOfNumber = int(input("x:"))

for i in range(5):
    print('*' * (5-i))
    time.sleep(0.3)
print("-------")
print("| ", random.randint(1, rangeOfNumber), " |")
print("-------")

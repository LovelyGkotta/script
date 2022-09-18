import random
import time
rangeOfNumber = int(input("press the side of dice"))
for i in range(5):
    print('*' * (5-i))
    time.sleep(0.3)
print("-------")
print("| ", random.randint(1, rangeOfNumber), " |")
print("-------")

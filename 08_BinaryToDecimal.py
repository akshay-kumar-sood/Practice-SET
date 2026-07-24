# Binary TO Decimal

import math
binary_number=input("Enter binary : ")
power=0
decimal_number=0

for i in reversed(binary_number):
    if i=='1':
        decimal_number+=math.pow(2,power)
    power+=1

print(f"decimal representation of {binary_number} is {decimal_number:.0f}")
# Prime Range ANalyzer

import math

num1=int(input("ENter number 1 : "))
num2=int(input("ENter number 2 : "))
count=0

def isPrime(num:int) -> bool:
    ''' identity no as prime or not'''
    if(num<=1):
        return False

    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True


for num in range(num1,num2+1):
    if(isPrime(num)):
        count+=1

print(count)

    
# make function to find isPrime or not.
# if less than 1 direct return False
# looop from 2 to sqrt to num
# if num divisible by any no means it is not isPrime

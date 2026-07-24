# ArmStrong NUmber Checker

import math
number=int(input("Enter number : "))
number_copy=number
total=0
digit=0

# count no of digit
while(number>0):
    digit+=1
    number=number//10

number=number_copy
# main logic
while(number>0):
    total+=math.pow((number%10),digit)
    number=number//10

total=int(total)


# just to comfirm
#print(total,number_copy,sep='\n')
res="YES" if total==number_copy else "NO"
print(res)


# note
# 10/3  ---> given floor division it give 3.33333
# 10/3  ---> give int it give 3

# Exam Result Processor

import math

m1=int(input("ENter marks of subject 1 : "))
m2=int(input("Enter marks of subject 2 : "))
m3=int(input("Enter marks of subject 3 : "))
m4=int(input("Enter marks of subject 4 : "))
m5=int(input("Enter marks of subject 5 : "))
avg=(m1+m2+m3+m4+m5)/5

if(m1<35 or m2<35 or m3<35 or m4<35 or m5<35):
    print("FAIL hahaha")


elif(avg>=75):
    print("DISTINCTION")

else:
    print("PASS")


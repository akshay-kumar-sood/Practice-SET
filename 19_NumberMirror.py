# Number Mirror Validator

number=int(input("ENter a number : "))
str=str(number)

reversed_str=str[::-1]

if(str==reversed_str):
    print("YES Palindrome")
else:
    print("Not a palindrome")


# note
#python slicing

# [start:stop:step]
# if step is positive start=0 stop=len-1

# when step is negative everything is reversed
# start=len-1 stop=-1 

#use [::-1] to reverse a string
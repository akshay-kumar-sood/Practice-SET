# Digital LOck Countdown

number=int(input("Enter a number : "))

# first loop run until number is greater then 10
while(number>=10):
    sum=0

    # find sum of curr number
    while(number>0):
        sum+=number%10
        number //=10;
    number=sum

print(number)


# question is faulty
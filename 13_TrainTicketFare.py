#Train Ticket Fare Calculator

distance=int(input("Enter total distance : "))
age=int(input("Enter age : "))

total_fare=distance*2

if(age>60):
    total_fare-=total_fare*0.3

elif(age<12):
    total_fare-=total_fare*0.5

print(f"Total Fare is : {total_fare:.0f}")
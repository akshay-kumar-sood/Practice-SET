# SMart Door Lock System

correct_pin=input("ENter correct pin : ")
attempt=0
flag=False

while(attempt<=2):
    attempt+=1
    user_pin=input("Enter pin ")
    if(user_pin == correct_pin):
        print("ACCESS GRANTED")
        flag=True
        break

if(flag==False):
    print("LOCKED")
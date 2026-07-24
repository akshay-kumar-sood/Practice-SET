# Traffic SIgnal Simulator

time=int(input("Enter time : "))

if(1<=time<=30):
    print("RED")
elif(31<=time<=45):
    print("YELLOW")
else:
    print("GREEN")
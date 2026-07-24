# Water Tank OverFLow Detector

n=int(input(" ENter N : "))
total=0
cnt=0

while(n>0):
    water=int(input("Enter water value : "))
    cnt+=1
    n-=1
    total+=water
    if(total>=1000):
        print(cnt)
        break


print("Cannot Overflow")
# Online Order Discount Engine

amount=int(input("ENter amount : "))

if(3000>amount>=1000):
    amount-=amount*0.05

if(5000>amount>=3000):
    amount-=amount*0.1

elif(amount>=5000):
    amount-=0.2*amount;

print(f" Final Amount is {amount:.0f}")

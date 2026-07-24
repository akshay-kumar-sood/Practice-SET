# Smart Electricity Billing

units=int(input("Enter electricity units : "))
initial=units
total=0

if(units>=100):
    total+=100*3
    units=units-100

    if(units>=100):
        total+=100*5
        units=units-100

        if(units>0):
            total+=8*units;

    else:
        total+=units*5;

else:
    total+=units*3

    

if(initial>350):
    total+=total*0.1

print(int(total))





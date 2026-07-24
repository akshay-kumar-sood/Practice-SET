# ATM TRANSACTION VALIDATOR

initial_balance = int(input("Enter initial balance: "))
total_balance=initial_balance
req=int(input("ENter no of requests : "))

for i in range(req):
    
    withdraw_amt=int(input("enter withdraw amount : "))
    temp_balance=total_balance-withdraw_amt;
    if(temp_balance>0 and withdraw_amt%100==0):
        total_balance-=withdraw_amt
        print("SUCCESS")
    else:
        print("FAILED")

print(total_balance)
    

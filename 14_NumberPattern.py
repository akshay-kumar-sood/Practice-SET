#Number Pattern Validator

number=int(input("Enter a number :"))

str=str(number)

def check(str) -> bool:
    for i in range(0,len(str)-1):
        if(str[i+1]< str[i]):
            return False

    return True

res="YES" if check(str) else "NO"

print(res)


# in java res = str==true ? "YES" : "NO"
# ternarry operator in java 
# in python 
# RES="YES" if check(str) else "NO"

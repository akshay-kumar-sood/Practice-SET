password=str(input("Enter a password : "))

if(
    len(password)>=8 and 
    any(ch.isalpha() for ch in password) and
    any(ch.isupper() for ch in password)
    ):
    print("STRONG")

else:
    print("WEAK")




# Salary Deduction System

salary=int(input("Enter salary : "))
late_days=int(input("ENter late days : "))
absent_days=int(input("Enter absent days : "))

if(10>late_days>5):
    salary-=0.05*salary

if(late_days>10):
    salary-=0.1*salary

if(absent_days>2):
    salary-=salary*0.05

print(f"Final salary is : {salary:.0f}")
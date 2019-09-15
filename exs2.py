"""
get three numbers and check if one of them equals to others
"""
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    num3=int(input("Enter a number:"))
    if num1==sum(num2,num3) or num2==sum(num1,num3) or num3==sum(num2,num1):
        print("It was found!!")
except ValueError:
    pass

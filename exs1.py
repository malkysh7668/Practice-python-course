"""
get a number and check if it's a even
"""
try:
    num=int(input("Enter a number:"))
    if num%2==0:
        print("it's a even number")
    else:
        print("it's a negative number")
except ValueError:
    print("You have not entered a value type number")

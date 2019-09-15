"""
calculator
"""
def input_number():
    while True:
        try:
            return int(input())
        except ValueError:
            pass

def calculator(n1,op,n2):
    if op=="+":
        res=n1+n2
    elif op =="-":
        res=n1-n2
    elif op =="*":
        res=n1*n2
    elif op =="/":
        res=n1/n2
    elif op =="^":
        res=n1**n2
    return res

num1=input_number()
num2=input_number()
operator=input("Enter a operator: (+,-,*,/,^)")
try:
    res=calculator(num1,operator,num2)
    print(f"{num1}{operator}{num2}=",res)
except ValueError:
    pass


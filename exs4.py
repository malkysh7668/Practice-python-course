"""
print a pyramid with space
"""
num=int(input())
cols=(2*num)-1
middle=int(cols/2)
for i in range(num):
    for j in range(cols):
        if abs(j-middle)<=i:
            print("*", end="")
        else:
             print(" ", end="")
    print()


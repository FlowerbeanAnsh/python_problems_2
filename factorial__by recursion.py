# FACTORIAL
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
num=int(input("enter the positive no:"))
out=fact(num)
print(out)

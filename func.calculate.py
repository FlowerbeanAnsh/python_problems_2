def calculate(a,b):
    if op=='+':
        c=a+b
        return c
    elif op=='-':
        d=a-b
        return d
    elif op=='*':
        e=a*b
        return e
    elif op=='/':
        f=a/b
        return f
    elif op=='%':
        g=a%b
        return g
    else:
        return False
f=float(input("enter the first value:"))
s=float(input("enter the second value:"))
op=input("enter the operation:")
result=calculate(f,s)
if result==False:
    print("your entered operation is not valid,please try again!!!")
else:
    print("your result is",result)
    
    

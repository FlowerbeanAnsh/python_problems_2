def greater_value(a,b):
    if a>b:
        return a
    else:
        return b
f=float(input("enter the first value:"))
l=float(input("enter the second value:"))
greater=greater_value(f,l)
if greater==f:
    print("the greater value is %f",f)
else:
    print("the greater value is %f",l)

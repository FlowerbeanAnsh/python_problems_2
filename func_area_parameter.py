def area_rectangle(a,b):
    return a*b
def parameter_rectangle(a,b):
    return 2*(a+b)
l=float(input("enter the length:"))
w=float(input("enter the weirth:"))
area=area_rectangle(l,w)
parameter=parameter_rectangle(l,w)
print("the area is=",area)
print("the parameter is=",parameter)

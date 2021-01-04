#reduce
from functools import reduce
my_fun=lambda x1,x2:x1 * x2
lst=list(map(int,input("enter list elements:").split()))
out=reduce(my_fun,lst)  #here reduce is taking elements from the list [(x1=1,x2=2),(x1=2,x2=4),(x1=8,x2=5),(x1=40)]
print("multiply is=",out)

f=lambda n:n*f(n-1) if n>0 else 1
n=int(input("enter the no:"))
fact=f(n)
print(fact)

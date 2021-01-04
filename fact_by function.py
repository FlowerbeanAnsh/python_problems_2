def fact(n):
    f=1
    for i in range(1,n+1):
        factorial=f * i
        return factorial
n=int(input("enter the no:"))
facto=fact(n)
print(facto)
        
        

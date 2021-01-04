lst=list(map(int,input("enter elements:").split()))
factorial_list=lambda n:n*factorial_list(n-1) if n>0 else False
out=list(map(factorial_list(lst)))
print(out)

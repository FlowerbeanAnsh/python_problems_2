lst=list(map(int,input("enter list elements:").split()))
only_even=lambda x:x%2==0
out=list(filter(only_even,lst)) #here filter is automaticly taking values from the list like map
print(out)

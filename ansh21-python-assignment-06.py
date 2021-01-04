#bottle necks problem
n =int(input("enter the num of bottels:"))
boq=input().split() 
dct=dict() 
sums= 0
for i in range(n): 
    dct[boq[i]] = dct.get(boq[i], 0) + 1
    sums = max(sums, dct[boq[i]])
print(dct)
print("minimum bottles are:=",sums)

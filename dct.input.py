dct={}
n=int(input("enter the range of dictionary:"))
for i in range(n):
    k=input("enter the key:")
    v=input("enter the value:")
    dct.update({k:v})
print(dct)

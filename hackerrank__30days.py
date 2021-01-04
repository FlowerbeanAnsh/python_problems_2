dct={}
n=int(input())
for i in range(n):
    name,no=input().split()
    dct[name]= no

for i in range(n):
    name=input()
    if name in dct:
        print("{}={}".format(name, dct[name]))
    else:
        print("Not found")



lst=list(map(int,input().split()))
lst1=[]
sums=0
for i in lst:
    sums = sums + ~(i)

if (sums%5)==0:
    print("yes")
else:
    print("no")

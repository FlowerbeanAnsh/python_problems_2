n=int(input())

sums=0
x=list(map(int,input().split()))
w=list(map(int,input().split()))

for i in range(len(x)):
    m= x[i] * w[i]
    sums=sums + m
nsum=sum(w)
print(sums)
print(nsum)
out=sums/nsum
print('%.1f'%out)

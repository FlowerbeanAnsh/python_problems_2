n,k=map(int,input().split())
n=int(n)
k=int(k)
h=list(map(int,input().split()))
m=max(h)
if m<k:
    print("0")
else:
    print(m-k)

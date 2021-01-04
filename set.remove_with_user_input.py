s=set()
n=int(input("enter the range:"))
for i in range(n):
    k=float(input())
    s.add(k)
print(s)
print(type(s))
s.remove(2)
print(s)

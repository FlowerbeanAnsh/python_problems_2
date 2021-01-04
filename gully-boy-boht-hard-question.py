s =input("enter string:")
lst=[]
lst1=[]
n = int(input("enter node point:"))
fr = int(input("enter frequency:"))
a = s[n::1]

for i in a:
    if i != ' ':
        lst.append(i)
b = s[0:n]
for i in b:
    if i!=" ":
        lst1.append(i)

t = lst + lst1

for i in range(fr):
    print(' '.join(t),end=' ')

s=input()
t=input()
lst1=[]
lst2=[]
lst3=[]
for i in s:
    lst1.append(int(i))

for i in t:
    lst2.append(int(i))

for i in range(len(lst1)):
    n=lst1[i] ^ lst2[i]
    lst3.append(n)

for i in lst3:
    print(i,end='')

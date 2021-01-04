s=input()
lst1=[]
lst2=[]
lst=[]
c=0
for i in s:
    for j in range(1,i):
        if i%j==0:
            c+=1
            lst1.append(i)
    else:
        lst2.append(i)
lst=lst1 + lst2

print(lst1)
print(''.join(lst))
    

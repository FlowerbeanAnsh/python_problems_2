n=6
lst=[-4,3,-9,0,4,1]
lst2=[]
c=0
t=0
g=0
for i in lst:
    if i > 0:
        c+=1

    elif i==0:
        t+=1

    else:
        g+=1

p=c/n
q=t/n
r=g/n

print(round(p,n))
print('%.6f'%q)
print('%.6f'%r)


n=int(input("enter the range:"))
dct={}
for i in range(n):
    
    name,*marks=input("enter the name and marks:").split()
    dct[name]=marks
qu=input("enter the quary name:")
tt=dct[qu]
print('%.2f'%(sum(map(eval,tt))/len(tt)))

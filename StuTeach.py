lst1=[]
lst2=[]
lst3=[]
for i in range(0,26):
    pos = chr(65+i)
    lst1.append(pos)



stu = input("enter the name of student:")
teach = input("enter the name of teacher:")

for j in stu:
    stor1 = lst1.index(j)
    lst2.append(stor1)
for k in teach:
    stor2 = lst1.index(k)
    lst3.append(stor2)
res1 = int("".join(map(str, lst2)))
res2 = int("".join(map(str, lst3)))

if res1 % 47 == res2 % 47:
    print("They Would be chosen")
else:
    print("Not chosen")

    
    

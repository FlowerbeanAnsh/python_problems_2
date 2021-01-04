a=eval(input("enter the list"))
b=eval(input("enter the sring which you want to find:"))
c=[]
for i in a:
    if i.startswith(a)==True:
        c.append(i)
print(c)

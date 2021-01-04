#sorry sir ,i could not done it by recursion method
def bitwise_and(lst1,lst2):
    lst3=[]
    if len(lst1) != len(lst2):
        return False
    else:
         for i in range(len(lst1)):
             t= lst1[i] & lst2[i]
             lst3.append(t)
         return lst3             

lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
out=bitwise_and(lst1,lst2)
print(out)

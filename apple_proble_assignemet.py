#problem 3
lst=list(map(int,input("enter list elements:").split()))
res=False

for i in range(len(lst)):
    if i == lst[i]:
        fix_value = i
        res = True
        break
if res  == True:
    print("the fixed value in given list is:",fix_value)
else:
    print("given list does not have any fixed value or point")
    

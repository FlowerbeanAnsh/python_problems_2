def vote_or_not(age):
    if age>=18:
        return True
    else:
        return False
ag=int(input("please enter your age:"))
res=vote_or_not(ag)
print(res)

canvote=lambda age:"you can vote" if age>=18 else "you can not vote!!"
current_age=int(input("enter your current age:"))
el=canvote(current_age)
print(el)

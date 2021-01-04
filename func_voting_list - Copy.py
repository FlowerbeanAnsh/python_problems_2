lst=list(map(int,input().split()))
canvote=lambda age:"you can vote" if age>=18 else "you can not vote!!"
out=list(map(canvote,lst))
print(out)

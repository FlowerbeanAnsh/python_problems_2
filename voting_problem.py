f=open("voting.txt","r")
m=[]
dc={}
fr=[]
for data in f:
    data=eval(data)
    if data[0] in m:
        fr+=[data[0]]
    else :
        m+=[data[0]]
        if data[1] not in dc.keys():
            dc.update({data[1]:1})
        else :
            dc.update({data[1]:dc[data[1]]+1})
top=sorted(dc.items(),key=lambda kv:(kv[1],kv[0]),reverse=True )
print("Top 3 candidate")
for i in range (3):
    print (top[i][0],"with votes",top[i][1])
if fr:
    print("people who did fraud")
    for i in fr:
        print(i)
f.close()

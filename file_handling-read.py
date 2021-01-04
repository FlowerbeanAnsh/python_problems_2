#read and readline
f= open("student.txt","rt")
#content=f.read(2)
#print(content)


for line in f:
    print(line,end='')
f.close()

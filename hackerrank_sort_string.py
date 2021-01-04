# Sample input=Sorting1234
#Sample Output=ginortS1324

st=input()
lower=[]
upper=[]
odd=[]
even=[]
sort=[]
for i in st:
    if i.isalpha():
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    else:
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
lower.sort()
upper.sort()
odd.sort()
even.sort()
sort=lower + upper + odd + even
print(''.join(sort))

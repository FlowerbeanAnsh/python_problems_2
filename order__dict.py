                        #output
                        #BANANA FRIES 12
                        #POTATO CHIPS 60
                        #APPLE JUICE 20
#input                        #CANDY 20
#BANANA FRIES 12
#POTATO CHIPS 30
#APPLE JUICE 10
#CANDY 5
#APPLE JUICE 10
#CANDY 5
#CANDY 5
#CANDY 5
#POTATO CHIPS 30
num=int(input("enter the range:"))
dct={}
for i in range(num):
    num , *key =input().split()[::-1]
    key =' '.join(key[::-1])
    if key in dct:
        dct[key] += int(num)
    else:
        dct[key] = int(num)
for i,j in dct.items():
    print(i ,j)


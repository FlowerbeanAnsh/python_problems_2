#number guess game by random
import random
random.seed(110)
sys=random.randint(1,100)
count=0
while 1:
    count+=1
    num=int(input("enter the number between 1 and 100:"))
    if sys > num:
        print("too small")
    elif sys < num:
        print("too large")
    else:
        print("right no!! you won")

print(count)


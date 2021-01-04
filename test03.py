n=int(input("enter a no:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    if i%3==0 and i%5!=0:
        print("fizz")
    if i%3!=0 and i%5!=0:
        print(i)
    if i%5==0 and i%3!=0:
        print("buzz")
        

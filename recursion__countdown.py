def countdown(n):
    if n==0:
        return "stop"
    else:
        print(n)
        countdown(n-1)
n=int(input("enter a no:"))
out=countdown(n)
print("happy recursion day")

    
    

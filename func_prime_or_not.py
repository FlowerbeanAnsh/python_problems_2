def prime_or_not(n):
    for i in range(2,n):
        if n%i==0:
            return "it is not a prime no"
    else:
        return "it is a prime no"
n=int(input("enter the no:"))
out=prime_or_not(n)
print(out)


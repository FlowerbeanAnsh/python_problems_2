def sum_ascii(a,b):
    def asci(*args_ANSH):   #taking multiple arguments
        c=ord(a)
        d=ord(b)
        return c+d
    return asci
n=input("enter the first character:")
m=input("enter the second character:")
lst=[n,m]
out=sum_ascii(*lst)
print(out())


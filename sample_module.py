def odd_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return "non prime no"
    else:
        return "prime no"
def sum_ascii(a,b):
    def asci(*myargs):
        c=ord(a)
        d=ord(b)
        return c+d
    return asci
def vote_or_not(age):
    if age<18:
        return "not eligible"
    elif age>=18:
        return "yes,you can vote"
    else:
        return "invalid data"
leap_year=lambda y:"leap year" if y%4==0 else "leap year" if y%400==0 and y%4!=0 else "ordinary year"

    


from sample_module import *
n=int(input("enter a no for checking odd even:"))
out=odd_even(n)
print("the no is",out)

t=int(input("enter a no for checking prime:"))
outp=prime(t)
print("the no is",outp)

a=int(input("enter a no for checking factorial:"))
output=fact(a)
print("fact of",a,"is",output)

v=int(input("enter your age:"))
votee=vote_or_not(v)
print(votee)

l=int(input("enter the year which youn want to check for leap year:"))
leap=leap_year(l)
print(leap)

m=input("enter the 1st character:")
o=input("enter the second character:")
asc=sum_ascii(m,o)
print(asc())


leap_year=lambda y:"leap year" if y%4==0 else "leap year" if y%400==0 and y%4!=0 else "ordinary year"
y=int(input("enter the year which you want to check:"))
out=leap_year(y)
print(out)

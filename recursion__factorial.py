#factorial by recursion
def fact_recurfun(n):
    if n==1:
        return n
    else:
        return n * fact_recurfun(n-1) #here this caling of function is called recursion

num=int(input("enter the num:"))
if num < 0:
    print("not possible!!")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("the factoial of",num,"is=",fact_recurfun(num))

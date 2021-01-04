#fibonacci series by lambda function

from functools import reduce
fibo_series=lambda n:reduce(lambda x1,x2:x1+[x1[-1] + x1[-2]],range(n-2),[0,1])

n=int(input("please enter the no whose you want to fibonacci series:"))
series=fibo_series(n)
print(series)

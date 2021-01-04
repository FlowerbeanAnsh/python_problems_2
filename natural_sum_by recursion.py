#natural sum of num
def natu_sum(n):
    if n==0:
        return 1
    else:
        return n + natu_sum(n-1)
num=int(input("enter the positive no:"))
out=natu_sum(num)
print(out)


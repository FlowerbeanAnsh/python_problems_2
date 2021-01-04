def palindrome_or_not(n):
    rev=0
    temp=n
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
        if rev==temp:
            return True
        else:
            False
n=int(input("enter the no:"))
t=palindrome_or_not(n)
if t==True:
    print("entered no is a palindrome no.")
else:
    print("non palindrome no")
        

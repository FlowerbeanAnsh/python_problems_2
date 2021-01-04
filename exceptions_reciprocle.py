#reciprocle of no
try:
    
    lst=input("enter the elements of list:").split()
    out=[]
    for i in range(len(lst)):
        out.append(1/i)
    print(out)

except ZeroDivisionError:
    print("error occured !!")

except EOFError:
    print("error ocured !!")

except KeyboardInterrupt:
    print("error occured !!")

else:
    print("your code is running successfully")













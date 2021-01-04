#wrong dict input by the user

try:
    n = int(input("enter the range:"))
    dct={}
    for i in range(n):
        keys = input("enter the keys:")
        values = input("enter the values:")
        dct.update({keys:values})
    print(dct)

except ValueError:
    print("please enter the valid range")


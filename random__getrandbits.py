#random getrandbits
import random

n=int(input("enter the bit size:"))
out=random.getrandbits(n)    # 0 to 2^n - 1
print(out)

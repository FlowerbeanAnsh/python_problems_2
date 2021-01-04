# shuffle
import random
def my_fun(ls):
    k = ls.copy()
    ls.clear()
    while k:
        x = random.choice(k)
        ls.append(x)
        k.remove(x)




lst = ['chanchal',  'bhavya', 'dheeraj', 'alok', 'lakshay']
print(lst)
my_fun(lst)
print(lst)

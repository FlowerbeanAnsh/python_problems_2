#choice method of random module
import random
lst=['ansh','ayush','abhishek','shivam','vansh']
out=random.choice(lst)
print(out)


#choices method of random module

out2=random.choices(lst,k)
print(out2)


out3=random.choices(lst,weights=[1,1,1,1,1],k=5)
print(out3)

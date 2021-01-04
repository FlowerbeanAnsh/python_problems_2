#random.triangular with math.ceil and math.floor
import random
import math
out=random.triangular(1,15,4)
print(out)   #returns a float value b/w 1 and 15 near by 4
output=math.floor(out)
print(output)          #convert float value into int(max to min)     
n_out=math.ceil(out)
print(n_out)           #convert float value into int(min to maxs) 

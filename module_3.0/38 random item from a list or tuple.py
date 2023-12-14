#  How can you pick a random item from a list or tuple? 

import random

tup = (12,23,45,'jk','ahir',)
print(tup)

randomitem = random.choice(tup)

print("random choice is : ",randomitem)
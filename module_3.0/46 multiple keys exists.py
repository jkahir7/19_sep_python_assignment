# Write a Python program to check multiple keys exists in a dictionary


dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'a',7:'a',}

count = 0

for k in dict1:
    count+=1
if count>1:
    print("multiple keys exists")

else:
    print("multiple keys not exists")
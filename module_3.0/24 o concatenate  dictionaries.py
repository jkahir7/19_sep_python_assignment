# Write a Python script to concatenate following dictionaries to create a new one.

a = {'jk':12,'ahir':22,'hello':32}

b = {'python':1,'java':2,'php':3}

dict = {}
for d in (a,b):
    dict.update(d)

print(dict)
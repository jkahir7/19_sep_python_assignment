# Write a Python program to convert a list of tuples into a dictionary.

tuple = [("sub1",66),("sub2",70),("sub3",90),("sub4",79)]

print(tuple)

dict1 = {}

for key,val in tuple:
    dict1[key] = val

print(dict1)
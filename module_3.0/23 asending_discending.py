# Write a Python script to sort (ascending and descending) a dictionary by value.

dict = {1:'jay',2:'deep',3:'jinal'}
print(dict)
ascending = sorted(dict.items())
print("ascending : ",ascending)

descending = sorted(dict.items(),reverse=True)
print("descending : ",descending)

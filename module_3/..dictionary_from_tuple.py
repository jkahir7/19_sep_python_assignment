# How will you create a dictionary using tuples in python?

tuple = (("jaydip",3),("paras",10),("jinal",9),("bhavin",45))
print(tuple)
dictionary = {}
for key, val in tuple:
    dictionary[key]=val

print(dictionary)
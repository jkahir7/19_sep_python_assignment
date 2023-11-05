# Write a Python script to check if a given key already exists in a dictionary.

def chechkey(dict,key):
    if key in dict.keys():
        print("key is already exists")

    else:
        print("key is not exists")

dict = {
    'a': 100,
    'b':200,
    'c':300
    }
key = 'a'
chechkey(dict,key)


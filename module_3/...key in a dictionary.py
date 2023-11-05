#  How Do You Check The Presence Of A Key In A Dictionary? 

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


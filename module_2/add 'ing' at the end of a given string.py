#    Write a Python program to add 'ing' at the end of a given string (length
#   should be at least 3). If the given string already ends with 'ing' then add
#    'ly' instead if the string length of the given string is less than 3, leave it
#    unchanged. 


string = input("enter a string : ")

if len(string) > 3 :

    if string.endswith("ing"):
        n_string = string + 'ly'
        print(n_string)

    else:
        n_string = string + 'ing'
        print(n_string)
else:
    print("string remain unchanged")
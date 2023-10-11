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
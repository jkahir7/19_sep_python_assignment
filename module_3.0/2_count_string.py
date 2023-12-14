# Write a Python program to count the number of strings where the string
#  length is 2 or more and the first and last character are same from a given list of strings.

string = input("enter a string : ")

if len(string) > 2:

    if string[:1] == string[-1:]:
        l1 = len(string)
        print(l1)

    
    else:
            print("first and last char is not same")
        
else:
    print("string is very short")

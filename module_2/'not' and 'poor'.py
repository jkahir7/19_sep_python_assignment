#    Write a Python program to find the first appearance of the substring
#   'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#    whole 'not'...'poor' substring with 'good'. Return the resulting string.

string=input("Enter String :- ")  # input a string

if str.startswith("not poor"):

    # it will replace "not poor" in "good"
    n_str=str.replace("not poor","good").lower() 
    print(n_str)

else:
    print(str)
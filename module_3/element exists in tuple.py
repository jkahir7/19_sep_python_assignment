# Write a Python program to check whether an element exists within a tuple


t = (1,3,5,7,9,6)

user = int(input("enter a number"))

for i in t:
    if user == i:
        print("element exists with tuple")
        break
    else:
        status = False
        print(status)


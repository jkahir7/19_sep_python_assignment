# Write a Python program to check whether a list contains a sub list


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [2,4,6,8]
l3 = []


for i in l2:
    if i in l1:  # check a element is already in l2 or not
        l3.append(i)

if l3 == l2:
    print("list contains a sub list")
else:
    print("not cointains sub list")
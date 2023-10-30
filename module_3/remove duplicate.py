
#  Write a Python program to remove duplicates from a list.


l1 = [23,34,65,57,78,89,89]

l2 = []  # empty string

for i in l1:
    if i not in l2:   # check a element is already in l2 or not
         l2.append(i)  # add value in l2
print(l2)    

# Write a Python program to get unique values from a list

l1 = [1,2,3,1,2,3,4,5,6]

l2 = []

for i in l1:
    if i not in l2:  # check a element is already in l2 or not
        l2.append(i)

print(l2)
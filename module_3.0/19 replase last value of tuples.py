# Write a Python program to replace last value of tuples in a list.

tup = (1,2,3,4,5,6)
l1 = list(tup)

l1[5] = 45

tup = tuple(l1)
print(tup)
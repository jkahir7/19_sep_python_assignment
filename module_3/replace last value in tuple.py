# Write a Python program to replace last value of tuples in a list

tup = (12,13,34,45,56,67,877,78)
l1 = list(tup)   #convert tuple into list

l1[7] = 1

tup = tuple(l1)   # re-convert into tuple

print(tup)
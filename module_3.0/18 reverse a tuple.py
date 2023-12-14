# Write a Python program to reverse a tuple.

def reverse(t):
    new_tup = t[::-1]
    return new_tup

t = (1,2,3,4,5,6,7,8)
print(reverse(t))

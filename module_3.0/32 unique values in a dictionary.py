# Write a Python program to print all unique values in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

unique_values = set(my_dict.values())

for value in unique_values:
    print(value)
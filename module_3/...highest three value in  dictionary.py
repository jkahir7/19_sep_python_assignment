#  Write a Python program to find the highest 3 values in a dictionary 


def highest_three(dictionary):
    values = list(dictionary.values())
    values.sort(reverse=True)
    return values[:3]

dictionary = {'a': 9, 'b': 8, 'c': 7, 'd': 4, 'e': 5, 'f': 6, 'g': 3, 'h': 2, 'i': 1}
print(highest_three(dictionary))
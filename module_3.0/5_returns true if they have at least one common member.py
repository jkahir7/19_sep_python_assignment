# Write a Python function that takes two lists and returns true if they have at least one common member

list1 = [1,55,67,3]
list2 = [3,56,76,4]

for i in list1:
    for j in list2:
        if i == j :
            print("true")

        else:
            print("false")
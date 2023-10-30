# Write a Python program to find the repeated items of a tuple.

tup = (23,34,456,57,78,34,57)
l1 = []
for i in tup:  
    if i not in l1:
        l1.append(i)  # value store without repet in l1
    
    elif i in l1:    
        print("repeted value is = ",i)
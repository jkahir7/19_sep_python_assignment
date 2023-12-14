# Write a Python program to remove an empty tuple(s) from a list of tuples.


tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),   # tuples in list
          ('krishna', 'akbar', '45'), ('', ''), ()]

for i in tuples:
        if len(i) == 0:
             tuples.remove(i) 

print(tuples)
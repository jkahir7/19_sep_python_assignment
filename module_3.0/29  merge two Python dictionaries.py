#  Write a Python script to merge two Python dictionaries 
s1 = {
       'name':'jk',
       'id':1
       }
s2 = {
   'class':'a',
   'age':21
   }

s = s1.copy()
s.update(s2)
print("Original dictionaries:")
print(s1)
print(s2)
print("\nMerge dictionaries:")
print(s)



#  Write a Python program to find the second smallest number in a list.

list1 = ['1','3','5','7','9']

list1.remove(min(list1)) # remove smallest number

print(" second small value = : ",min(list1))
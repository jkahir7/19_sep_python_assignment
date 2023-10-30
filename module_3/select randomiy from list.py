# Write a Python program to select an item randomly from a list. 

l1 = ["i","a","m","j","k","a","h","i","r"]
l2 = []
import random
for i in range(1,6):
    l2 = random.choice(l1)
    print(l2)
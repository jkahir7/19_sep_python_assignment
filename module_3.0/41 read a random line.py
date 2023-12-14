# Write a Python program to read a random line from a file.

import random

line = open('theory.txt').read().splitlines()

print(random.choice(line))
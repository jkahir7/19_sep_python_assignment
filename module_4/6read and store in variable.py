#Write a Python program to read a file line by line store it into a variable.
f=open("mynote1.txt","r")
a=""
lines=f.readlines()
for i in lines:
    a+=i

print(a)
#Write a Python program to read a file line by line and store it into a list
f=open("mynote1.txt","r")
list1=[]
lines=f.readlines()
for i in lines:
    print(i)
    list1.append(i)

print(list1)
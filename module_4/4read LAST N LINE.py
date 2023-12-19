#Write a Python program to read last n lines of a file.
f=open("mynote1.txt","r")
n=int(input("enter a number of lines"))
lines=f.readlines()
for i in range(1,n+1):
    print(lines[-i])
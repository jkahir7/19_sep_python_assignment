import os
f=open("mynote1.txt","a")
line=f.read()

os.mkdir("mynote2")
f2 = open("mynote2.txt","a")


for line in f:
    print(line)
    f2.write("\n email = "+(line))

print(f2)


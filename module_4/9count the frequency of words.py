f=open("mynote1.txt","r")
line=f.read()
count=0
for i in line:
    count+=1

print(f"{count} world in file")



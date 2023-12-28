f=open("mynote1.txt","r")
lines=f.readlines()
count=0
for i in lines:
    count+=1

print(f"{count} lines i file")


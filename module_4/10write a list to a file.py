f=open("mynote1.txt","a")

a=input("enter a list")

list1=[]
list1.append(a)

print(list1)
f.write("\n list = "+str(list1))
f.close()
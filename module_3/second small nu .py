# Write a Python program to find the second smallest number in a list. 

l1 = []  # empty list

status = True
while status :
    user = int(input("enter number")) 
    l1.append(user)       # value add in l1
    print("do you want to add more ? :press 'y'for yes and 'n' for not ")
    choice = input("enter your")  
    if choice == "n":
        status = False

print("l1 = ",l1)
l1.remove(min(l1)) # remove smallest number

print(" second small value = : ",min(l1))
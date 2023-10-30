# Write a Python program to check whether a list contains a sub list

l1 = [12,23,34,45,56,67,78,89,43]
l2 = []
l3 = []
status = True
while status:
    user = int(input("enter your sub list"))
    l2.append(user)
    print("do you want to add more : press y for yes or n for not")
    choice = input("enter your choice")
    if choice == 'y':
        status = True
    else:
        status = False


print(" l1 = ",l1)
print(" l2 = ",l2)

for i in l2:
    if i in l1:  # check a element is already in l2 or not
        l3.append(i)
print("l3 = ",l3)
if l3 == l2:
    print("list contains a sub list")
else:
    print("not cointains sub list")
# Write a Python function to get the largest number, smallest num and sum of all from a list. 

list = []
sum = 0

for i in range(1,6):

    user = int(input("enter a numbers : "))
    sum += user
    list.append(user)


print("maximum num is : ",max(list))
print("small num is : ",min(list))
print("sum of string is : ",sum)
# Write a Python function to get the largest number, smallest num and sum of all from a list. 


list = []  # empaty list
sum = 0
for i in range(1,6):

    user = int(input("enter numbers : "))
    sum+=user  #sum = sum + use
    list.append(user)  # input add to list

print("maximum num is : ",max(list))
print("small num is : ",min(list))
print("sum of string is : ",sum)
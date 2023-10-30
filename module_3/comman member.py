list = [34,45,57,2,78,89] 
list_2 =[2,33,44]

for i in list:
    for j in list_2:
     if i == j :
      break
      print("true")    
else:
    print("false")
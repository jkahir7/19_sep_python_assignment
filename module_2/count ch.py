string = "this is a lectur of python"
count = 0
#Counts  character except space.
for i in range(0, len(string)):
   if(string[i] != ' '):
      count = count + 1
#Displays the total number of characters .
print("Total number of characters in a string: " + str(count))

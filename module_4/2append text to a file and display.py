#Write a Python program to append text to a file and display the text.

id = int(input("enter id : "))
name = input("enter your namr : ")
subject = input("enter a subject : ")

f = open("mynote1.txt","a")

f.write("\n id = "+str(id))
f.write("\n name = "+(name))
f.write("\n subject = "+(subject))

f.close()
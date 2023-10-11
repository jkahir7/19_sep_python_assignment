#Write a Python program to get the Fibonacci series of given range 

num=int(input("Enter a number  :- "))
x=0
y=1
print(x)
print(y) 
 
for i in range (2,num):
    
    num=x+y
    print(num)
    x,y=y,num
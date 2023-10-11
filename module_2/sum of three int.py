# sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))

sum=0
if a==b or b==c or a==c:
    print("sum is zero")

else:
    sum=a+b+c
    print("sum is :",sum)

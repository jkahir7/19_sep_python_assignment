#  Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero

a=int(input("Enter First num : "))
b=int(input("Enter Second num : "))
c=int(input("Enter Third num : "))

# check any two num is equl or not
if a == b or b == c or c == a:
    print("Two Integers are equal")
    sum = 0
else:
    sum= a + b + c
    
print(f"sum of {a} + {b} + {c} = {sum}")
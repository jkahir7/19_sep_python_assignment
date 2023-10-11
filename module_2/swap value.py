# swap values

a=20
b=10

temp=a
a=b
b=a
b=temp

print(f"a is with temp = {a} and b is with temp ={b}")

a,b=b,a
print(f"a is = {a} and b is  ={b}")


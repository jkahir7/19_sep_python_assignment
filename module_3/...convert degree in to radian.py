

pi = 22/7

def convert_degree(degree):
    radian = degree * (pi/180)
    return radian

degree = float(input("enter a value of degree : "))
radian = convert_degree(degree)
print(f"The radian value is: {radian}")
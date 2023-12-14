# Write a Python program to convert degree to radian



pi = 22/7

def convert_(degree):
    radian = degree * (pi/180)
    return radian

degree = float(input("enter a value of degree : "))
radian = convert_(degree)
print(f"The radian value is: {radian}")
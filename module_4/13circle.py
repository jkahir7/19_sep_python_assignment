#Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

Circle1 = Circle(8)
print(Circle1.area())
print(Circle1.perimeter())
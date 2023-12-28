#Write a Python class named Rectangle constructed by a length and
#width and a method which will compute the area of a rectangle

class rectangle():
    def __init__(self,l,w):
        self.lenth=l
        self.width=w

    def area(self):
        return self.lenth*self.width
    
obj = rectangle(10,5)
print(obj.area())
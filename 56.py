import math

class Shape:  # Interface
    def input(self): pass
    def process(self): pass
    def output(self): pass

class Circle(Shape):
    def __init__(self, rad=0.0):
        self.radius = rad
        self.area = 0.0

    def input(self):
        self.radius = float(input("Enter radius: "))

    def process(self):
        self.area = math.pi * math.pow(self.radius, 2)

    def output(self):
        print("Circle Area:", self.area)

class Rectangle(Shape):
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth
        self.area = 0

    def input(self):
        self.length = int(input("Enter Length: "))
        self.breadth = int(input("Enter Breadth: "))

    def process(self):
        self.area = self.length * self.breadth

    def output(self):
        print("Rectangle Area:", self.area)

# Create instances and call methods
c = Circle()
c.input()
c.process()
c.output()

r = Rectangle()
r.input()
r.process()
r.output()

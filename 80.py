from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create instances of Circle and Rectangle
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)

# Calculate and display areas
print(f"Area of the circle: {circle.area()}")
print(f"Area of the rectangle: {rectangle.area()}")

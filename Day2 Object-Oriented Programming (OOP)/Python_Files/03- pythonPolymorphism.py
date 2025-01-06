# Parent class
class Shape:
    def area(self):
        pass  # Define a generic method

# Child class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Child class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Demonstrating polymorphism
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"The area of the shape is: {shape.area()}")
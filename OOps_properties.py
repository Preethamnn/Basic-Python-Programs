# Import ABC and abstractmethod to create an abstract class
from abc import ABC, abstractmethod

# Create an abstract class
class Shape(ABC):

    # Constructor to initialize area
    def __init__(self):
        self.area = 0

    # Abstract method to take input
    @abstractmethod
    def collect(self):
        pass

    # Abstract method to calculate area
    @abstractmethod
    def calculate(self):
        pass

    # Method to display the area
    def display(self):
        print("Area =", self.area)


# Circle class inherits Shape
class Circle(Shape):

    # Take radius from user
    def collect(self):
        self.r = float(input("Enter radius: "))

    # Calculate area of circle
    def calculate(self):
        self.area = 3.14 * self.r * self.r


# Rectangle class inherits Shape
class Rectangle(Shape):

    # Take length and breadth from user
    def collect(self):
        self.l = float(input("Enter length: "))
        self.b = float(input("Enter breadth: "))

    # Calculate area of rectangle
    def calculate(self):
        self.area = self.l * self.b


# Square class inherits Shape
class Square(Shape):

    # Take side from user
    def collect(self):
        self.side = float(input("Enter side: "))

    # Calculate area of square
    def calculate(self):
        self.area = self.side * self.side


# Geometry class
class Geometry:

    # This method works for any shape
    def permit(self, shape):

        # Take input
        shape.collect()

        # Calculate area
        shape.calculate()

        # Display result
        shape.display()


# Create object of Geometry
g = Geometry()

# Create objects of all shapes
c = Circle()
s = Square()
r = Rectangle()

# Calculate area of circle
g.permit(c)

print("----------------")

# Calculate area of square
g.permit(s)

print("----------------")

# Calculate area of rectangle
g.permit(r)
# Open-Closed Principle -> The OCP states that the software entities (classes, modules, functions, etc) should be
# open to extension but closed to modification. In other words we should extend the behavior of a class without
# modifying its existing code

# The following code breaks OCP:

# class Shape:
#     def __init__(self, type):
#         self.type = type
#
#     def calculate_area(self):
#         if self.type == "circle":
#             radius = float(input("Enter the radius: "))
#             area = 3.14 * radius * radius
#             print("Area of the circle:", area)
#         elif self.type == "rectangle":
#             length = float(input("Enter the length: "))
#             width = float(input("Enter the width: "))
#             area = length * width
#             print("Area of the rectangle:", area)
#         # More elif statements for other shapes...
#
#
# shape = Shape("circle")
# shape.calculate_area()


# In this example Shape class has a method called calculate_area() that calculates the area based ot the shape type.
# However, whenever a new shape is added (eg. triangle), we would need to modify the calculate_area() method,
# violation the OCP

# --------------------------------------- Correct way --------------------------------------------------------------
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Add more shape sublcasses for other shapes


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def calculate_total_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.calculate_area()
        return total_area


# cicle = Circle(10)
# rectangle = Rectangle(5, 8)
#
# print(cicle.calculate_area())
# print(rectangle.calculate_area())
#
# areacalculator = AreaCalculator([cicle, rectangle])
#
# print(areacalculator.calculate_total_area())



import math

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self,   side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    #def area(self):
        #pass

    def perimeter(self):
        perimeter = self.__side_a + self.__side_b + self.__side_c
        return  perimeter

    def area(self):
        perimeter = self.__side_a + self.__side_b + self.__side_c
        half_p = perimeter /2
        area = math.sqrt(half_p *(half_p - self.__side_a) * (half_p - self.__side_b) * (half_p - self.__side_c))
        return area


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        area = math.pi * (self.__radius ** 2)
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.__radius
        return perimeter


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        area = self.__side_a * self.__side_b
        return area

    def perimeter(self):
        perimeter = 2 * (self.__side_a + self.__side_b)
        return perimeter

figure_circle = Circle(5)
print(f"area circle = {figure_circle.area()}")
print(f"perimeter circle = {figure_circle.perimeter()}")

figure_rectangle = Rectangle(5, 6)
print(f"area rectangle = {figure_rectangle.area()}")
print(f"perimeter rectangle = {figure_rectangle.perimeter()}")

figure_triangle = Triangle(3, 3, 3)
print(f"area triangle = {figure_triangle.area()}")
print(f"perimeter triangle = {figure_triangle.perimeter()}")
"""imported math module"""
import math


class Circle:
    """
    this is for the calculation of area and volume
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """

        :return:
        """
        return math.pi * radius ** 2

    def perimeter(self):
        """

        :return:
        """
        return 2 * math.pi * radius


class Rectangle:
    """
    this is for the calculation of rectangle
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        """

        :return:
        """
        return width * height

    def perimeter(self):
        """

        :return:
        """
        return 2 * (height + width)


class Cube:
    """
    this class is for the calculation of cube
    """
    def __init__(self, side):
        self.side = side

    def area(self):
        """

        :return:
        """
        return 6 * (side ** 2)

    def perimeter(self):
        """

        :return:
        """
        return 12 * side

    def volume(self):
        """

        :return:
        """
        return side ** 3


"""class sphere"""


class Sphere():
    """
    calculation of sphere
    """
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        """

        :return:
        """
        return 4 * math.pi * (radius ** 2)

    def volume(self):
        """

        :return:
        """
        return 4 / 3 * math.pi * (radius ** 3)


class Square:
    """
    calculation of sphere
    """
    def __init__(self, side):
        self.side = side

    def area(self):
        """
        :return:
        """
        return side ** side

    def perimeter(self):
        """

        :return:
        """
        return 4 * side


if __name__ == '__main__':
    while True:
        try:
            shape = input("Enter the shape (circle, rectangle, cube, sphere, square):")
            # user input
            if shape == "circle":
                radius = float(input("Enter the radius of the circle: "))
                circle = Circle(radius)
                print(f"Area: {circle.area()}")
                print(f"Perimeter: {circle.perimeter()}")

            elif shape == "rectangle":
                width = float(input("Enter the width of the rectangle: "))
                height = float(input("Enter the height of the rectangle: "))
                rectangle = Rectangle(width, height)
                print(f"Area: {rectangle.area()}")
                print(f"Perimeter: {rectangle.perimeter()}")

            elif shape == "cube":
                side = float(input("Enter the side length of the cube: "))
                cube = Cube(side)
                print(f"Area: {cube.area()}")
                print(f"Perimeter: {cube.perimeter()}")
                print(f"Volume: {cube.volume()}")

            elif shape == "sphere":
                radius = float(input("Enter the radius of the sphere: "))
                sphere = Sphere(radius)
                print(f"Area: {sphere.area()}")
                print(f"Volume: {sphere.volume()}")

            elif shape == "square":
                side = float(input("enter the side of square:"))
                square = Square(side)
                print(f"area:{square.area()}")
                print(f"perimeter:{square.perimeter()}")
            else:
                print("Invalid shape entered.")
        except ValueError as e:
            print(e)

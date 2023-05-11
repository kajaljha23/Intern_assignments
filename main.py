from scripts.core.handlers.circle import Circle
from scripts.core.handlers.cube import Cube
from scripts.core.handlers.rectangle import Rectangle
from scripts.core.handlers.sphere import Sphere
from scripts.core.handlers.square import Square

shape = input("Enter the shape (circle, rectangle, cube, sphere, square):")
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

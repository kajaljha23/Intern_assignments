import math
class Sphere():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius**2)

    def volume(self):
        return 4/3 * math.pi * (self.radius ** 3)
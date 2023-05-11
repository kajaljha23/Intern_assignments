class Cube():
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def perimeter(self):
        return 12 * self.side

    def volume(self):
        return self.side ** 3
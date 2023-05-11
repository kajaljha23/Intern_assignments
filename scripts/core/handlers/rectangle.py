class Rectangle():
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.height + self.width)
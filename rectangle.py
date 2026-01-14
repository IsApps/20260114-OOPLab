class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(5, 3)
print(rect1.area())
print(rect1.perimeter())

rect2 = Rectangle(10, 4)
print(rect2.area())
print(rect2.perimeter())

class Rectangle:
    def __init__(self, side=0, width=0):
        self.side = side
        self.width = width

    def area(self):
        if self.side > 0:
            return self.side ** 2
        elif self.side > 0 and self.width > 0:
            return self.side * self.width
        else:
            raise ValueError("Invalid rectangle dimensions.")


# Test the class
square = Rectangle(5)
print(square.area())  

rectangle = Rectangle(3, 4)
print(rectangle.area())  
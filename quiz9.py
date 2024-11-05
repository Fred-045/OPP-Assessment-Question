class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

vector1 = Vector(43, 24)
vector2 = Vector(51, 61)

resultant_vector = vector1 + vector2

print(resultant_vector.x)  
print(resultant_vector.y)  
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = 5
circle = Circle(radius)
area = circle.area()
perimeter = circle.perimeter()
print(f"Area of the circle with radius {radius} is: {area:.2f}")
print(f"Perimeter (circumference) of the circle with radius {radius} is: {perimeter:.2f}")
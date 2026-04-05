class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # IMPORTANT: iteration
    def __iter__(self):
        yield f"length: {self.length}"
        yield f"width: {self.breadth}"


# Test
r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())

# Iteration test
for i in r:
    print(i)
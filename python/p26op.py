class Demo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Demo(self.x + other.x)

    def __sub__(self, other):
        return Demo(self.x - other.x)

    def __mul__(self, other):
        return Demo(self.x * other.x)

    def __truediv__(self, other):
        return Demo(self.x / other.x)

    def __eq__(self, other):
        return self.x == other.x

    def __str__(self):
        return str(self.x)
a = Demo(10)
b = Demo(20)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a == b)

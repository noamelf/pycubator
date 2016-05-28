class Point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, other):
        return other.x - self.x, other.y - self.y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __sub__(self, other):
        return self.distance(other)

p1 = Point(3, 6)
p2 = Point(2, 4)

print(p2 - p1)

data = [p1, p2, p2 - p1]
print(data)

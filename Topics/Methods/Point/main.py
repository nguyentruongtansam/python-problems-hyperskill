import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other: 'Point'):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    pass

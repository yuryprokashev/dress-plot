class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{ x: " + self.x.__str__() + ", y: " + self.y.__str__() + " }"

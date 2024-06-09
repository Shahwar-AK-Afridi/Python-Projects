class Point:

    def __init__(self, initX, initY) -> None:
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        distance = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return distance
    
    def halfway(self, target):
        mid_x = (self.x + target.x)/2
        mid_y = (self.y + target.y)/2
        return Point(mid_x, mid_y)
    
class Rectangle:

    def __init__(self, p1, p2) -> None:
        """Initializes a new Rectangle object with two Point objects p1 and p2, representing the diagonally opposite corners of the rectangle."""
        self.p1 = p1  #composition in action
        self.p2 = p2

    def area(self):
        length = abs(self.p1.x - self.p2.x)
        width = abs(self.p1.y - self.p2.y)
        area_of_rectangle = length * width
        return area_of_rectangle
    
point1 = Point(10, 12)
point2 = Point(5, 6)

r1 = Rectangle(point1, point2)

print("Area of Reactangle:", r1.area())
    
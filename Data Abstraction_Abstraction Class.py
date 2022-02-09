from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def no_of_sides(self):
        print("I have 3 sides")

class Quadrilateral(Polygon):
    def no_of_sides(self):
        print("I have 4 sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def no_of_sides(self):
        print("I have 6 sides")

tri = Triangle()
quad = Quadrilateral()
penta = Pentagon()
hexa = Hexagon()

tri.no_of_sides()
quad.no_of_sides()
penta.no_of_sides()
hexa.no_of_sides()
    

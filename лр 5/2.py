class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        print('Радиус равен ' + str(self.radius))
    def set_radius(self, new_radius):
        self.radius = new_radius
class Elipse:
    

circle1 = Circle(3)

circle1.get_radius()
circle1.set_radius(11)
circle1.get_radius()


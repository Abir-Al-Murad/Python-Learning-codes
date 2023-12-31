class shap:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class circle(shap):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14 * super().area()

rec = shap(3,6)
print("Area of a Rectangular:", rec.area())

c = circle(5)
print("Area of a circle",c.area())

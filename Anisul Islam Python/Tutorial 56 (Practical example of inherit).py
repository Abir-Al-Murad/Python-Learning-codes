class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    # def area(self):
    #     print("I am area method of shape class")
class Triangle(shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("Area of Triangle: ",area)
class Rectenagle(shape):
    def area(self):
        area = self.dim1*self.dim2
        print("Area of Rectenangle: ",area)
tri = Triangle(12,30)
tri.area()
recten = Rectenagle(20,30)
recten.area()

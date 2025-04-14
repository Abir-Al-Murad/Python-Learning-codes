from abc import ABC,abstractmethod #abstruct class use kora hoy shudu model hisebe use korar jonno
class shape(ABC):                  #and take sobai iccha moto use korte parbe
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
        # print("Shape has no Area.")
        pass #amra shudu area method ta use korte chacchi tai pass kore dilam
class Triangle(shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("Area of Triangle: ",area)
class Rectenagle(shape):
    def area(self):
        area = self.dim1*self.dim2
        print("Area of Rectenangle: ",area)
# sp = shape(10,20)      #abstruct class er object toiri kora jay na
# sp.area()
tri = Triangle(12,30)
tri.area()
recten = Rectenagle(20,30)
recten.area()
#abstruct class use korbe area method use kortei hobe ei khetre
#abstruct class jei method e use kora hoy oi method er child class der oi method must use korte hoy ba call korte hoy

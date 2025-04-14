class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_area(self):
        x=(self.base*self.height)/2
        print("The Area of Triangle is : ",x)
t1 = Triangle(10,20)
t2 = Triangle(20,30)
t1.calculate_area()
t2.calculate_area()
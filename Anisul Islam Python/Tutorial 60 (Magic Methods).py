class Bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    #String Magic Method
    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}") #STRING sob somoy return korbe tai return keyword use korte hobe
    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = Bike("Yamaha R15","Blue")
bike2 = Bike("Yamaha R15","Red")
print(bike1)
#Equal operator ache ekta jeta ami kori ni but class e koriyeche
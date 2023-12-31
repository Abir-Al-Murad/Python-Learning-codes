class person:
    name = "CarryMinati"
    occupation = "Youtuber"
    networth = 10
    def info(self): #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        print(f"{self.name} is a {self.occupation}")

a= person() #a,b,c holo object
print(isinstance(a,person)) #a jodi person nam er class er object hoy tahole true return korbe
b= person()
c= person()
a.name = "Masud"
a.occupation = "Student"
b.name = "Mohiuddin"
b.occupation = "Freelancer"
a.info()
#info function niye na korle---->
print(f"{a.name} is a {a.occupation}")
b.info()
c.info()
print("***Done By Me***")
class product:
    name = "Shirt"
    brand = "Easy"
    price = 2000
    def info(self):
        print(f"Product name --> {self.name}\nBrand name is -->{self.brand}\nprice is -->{self.price}Tk \n")
a= product()
a.info()
b= product()
b.name = "T-shirt"
b.brand = "Puma"
b.price = 1299
b.info()
c = product()
c.name = "Underwear"
c.brand = "CR7"
c.price = 700
c.info()

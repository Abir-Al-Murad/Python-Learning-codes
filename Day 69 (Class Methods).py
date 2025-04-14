#custom data type bananor jonno class methods use kora hoy

class Emloyee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod # class er vitore j company ache seta directly change korbe
    def changeCompany(tinde,newcomany):
        tinde.company = newcomany

e1 = Emloyee()
e1.name = "Rakib"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Emloyee.company) #uporer class method ta use na korle company name "Apple" e thakto

class student:
    uni_name = "BracU"
    def __init__(self,name,id):
        self.name= name
        self.id = id
    def details(self):
        print("Name:",self.name, "ID:",self.id,student.uni_name)
    @classmethod
    def up_uni_name(cls,u_name):
        cls.uni_name = u_name

s1 = student("Rofiq",112)
s2 = student("Meshkat",120)
s1.details()
s2.details()
student.up_uni_name("Brac University") #student na diye s1 er reference e jodi change kortam tao sob gular varsity name change hoye jeto cz eta class er reference e change hoto
# s1.up_uni_name("Northern University Bangladesh")
s1.details()
s2.details()





class student:
    uni_name = "BracU"
    def __init__(self,name,id):
        self.name= name
        self.id = id
    def details(self):
        print("Name:",self.name, "ID:",self.id,self.uni_name) #changed student.uni_name to self.uni_name
    def update_uniname(self,u_name): #ager ta chilo class er under e r eta instance
        self.uni_name = u_name

s1 = student("Rofiq",112)
s2 = student("Meshkat",120)
s1.details()
s2.details()
s1.update_uniname("Brac University") #ei khetre only s1 er varsity name change hobe
s1.details()
s2.details()
print(s2.__dict__)

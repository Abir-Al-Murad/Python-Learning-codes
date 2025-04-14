class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = employee("Harry",12000)
print(e1.name)
print(e1.salary)


string = "John-12000"
e2 = employee(string.split("-")[0], string.split("-")[1])
print(e2.name)
print(e2.salary)

a = "Harry-12-Python"
print(a.split("-")) # split korle a string ti list e porinoto hobe




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)


            #Done by me
class genjam:
    def __init__(self,game,company):
        self.game = game
        self.company = company
    @classmethod
    def bb(cls,string2):
        return cls(string2.split("-")[0],string2.split("-")[1])

string2 = "Pubg-Tencent"
l = genjam.bb(string2)
print(l.game)
print(l.company)


            #Learn with Tawhid

class Student:
    uni_name = "NUB"
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print("Name:",self.name,"ID:",self.id,Student.uni_name)
    @classmethod
    def from_string(cls,info):
        name,id = info.split("-")
        obj = cls(name,id) #eta dile function ta __init__ e jay and obj holo location er reference
        return obj
s1 = Student("Masud",1388)
print(Student.from_string("Abir-1302"))
s2 = Student.from_string("Abir-1302") #Class Method er info te Abir-1302 jabe
s1.details()
s2.details()
s3 = Student.from_string("Maruf-1333")
s3.details()
s4 = Student("Sadia",1732)
s4.details()


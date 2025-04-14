class Employee:
    def __init__(self):
        self.name = "Kabir"
a = Employee()
print(a.name) # eta print hobe ba amra self.name er access nite parbo cz eta Public variable


#Private Access Modifier

class employee:
    def __init__(self):
        self.__name = "Maruf (private)" ##name er age __ dewoa mane eta private
b = employee()
# print(a.__name)   # evabe amra eta access nite parbo na cz eta private
print(b._employee__name) # But amra evabe likhe private e access nite pari etak bole Name Mangling
print(b.__dir__()) # b er upor j j method apply hoice ta show korbe
print(dir(b))

# Protected Access Modifier

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
# print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())

class parentclass:
    def parent_method(self):
        print("This is the parent method")
class Childclass(parentclass):
    def parent_method(self):
        print("Harry")
        super().parent_method() # super keyword is used to give access to methods and properties of a parent or sibling class
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
child_obj = Childclass()
child_obj.parent_method()
child_obj.child_method()



class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language = language
rohan = Employee("Rohan Hasan","1200")
Abir = Programmer("Abir Al Murad","1546","Python")
print(rohan.id)
print(Abir.name)
print(Abir.id)
print(Abir.language)
class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdata(self):
        print(f"The name of Employee: {self.id} is {self.name}")
class programmer(employee):
    def showlanguage(self):
        print("The default language is Python")
e1=employee("Junayeed",520)
e1.showdata()
e2 = programmer("Shihab",522) #programmer class e employee class o kaj koretese
e2.showdata()
e2.showlanguage()


class Emplyoee:
    CompanyName = "Apple" #class variable ja class er property and instance er property na
    noOfemployees = 0
    def __init__(self,name):
        self.name = name # instance variable
        self.raise_amount = 0.2 # instance variable
        Emplyoee.noOfemployees +=1
    def showdetails(self):
        print(f"The Name of the Employee is {self.name} and the raise amount in {self.noOfemployees} sized {self.CompanyName} is {self.raise_amount}")
# Creating Instance of Employee
emp1 = Emplyoee("Tamim")
emp1.raise_amount = 0.3
emp1.showdetails()
emp2 = Emplyoee("Mostafiz")
emp2.raise_amount = 0.9
emp2.showdetails()
# Accessing the class variable through an instance
# Modifying the class variable
emp2.CompanyName = "Apple India"

Emplyoee.CompanyName = "Google" # Class variable e change hoye jabe
emp3 = Emplyoee("Mithun")
emp3.raise_amount = 0.02
emp3.showdetails()


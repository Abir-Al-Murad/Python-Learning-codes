class A:
    def display1(self):
        print("I am inside A class.")

class B(A):
    # + Display1
    def display2(self):
        print("I am inside B class.")

class C(B):
    # + Display1 + Display2
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class.")
#Multilavel Inheritance: A class k jodi B class and B class k jodi
#C class inherite kore tahole take multilavel inherit bole
obj1 = C()
# obj1.display1()
# obj1.display2()
obj1.display3()
#Ekhane C class ei 3ta class kaj kortese
class L:
    def display(self):
        print("I am inside L class.")

class K:

    def display(self):
        print("I am inside K class.")

class J(K,L):
    pass
obj2 = J()
obj2.display() #Class j er moddeh age K diyechi tai er priority beshi r Class K print korbe
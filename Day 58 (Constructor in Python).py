class person():
    def __init__(self,n,o):
        print("Hey I am a person")
        self.name= n
        self.occ= o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a= person("Harry","Developer")
a.info()
b= person("Divya","HR")
b.info()
class hello():
    def __init__(self,x,y):
        print("Hello I am here")
        self.hola = x
        self.kola = y
    def info(self):
        print(f"Kire Hala {self.hola} valo hobi kobe? {self.kola}.")
a= hello("Valo Achis?","Ajk")
a.info()






print("****This is Easy to understand****")
class student:
    roll = ""
    gpa = ""
    def __init__(self,j,k):
        self.roll = j
        self.gpa = k
    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa} ")
rahim = student(101,3.75)
rahim.display()
karim = student(1302,4.00)
karim.display()



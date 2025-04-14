"""
 Amra jokhn chaibo j user 1 ta parameter dileo constructor kaj korbe abr 2/3/4 dileo consturctor kaj korbe
se khetre amra contructor overlaoding use korte pari.
"""
class student:
    def __init__(self,*info): # *info mane user tar iccha moto parameter dite parbe(unknown argument receive kore)
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.CGPA = info[2]
            print(f"{self.name}, ID : {self.id}, CGPA:{self.CGPA}")
        elif len(info) == 2:
            self.name = info[0]
            self.id = info[1]
            print(f"{self.name}, ID : {self.id}")
        elif len(info) == 1:
            self.name = info[0]
            print(f"{self.name}")
        # print("A student object created")

s1 = student("shihab",1755,2.50)
s2 = student("Abir",1302)
s3 = student("Masud")
s4 = student("sayeed",1590,3.50)


print("*****Unknown Number of Keyword Argument******")

class student1:
    def __init__(self,**info): # (**info means unknown number of keyword argument)
        if len(info) == 3:
            self.name = info["name"]
            self.id = info["id"]
            self.cgpa = info["cg"]
            print(f"{self.name}\nID :{self.id}\nCGPA:{self.cgpa}")
        elif len(info) == 2:
            self.name = info["name"]
            self.id = info["id"]
            print(f"\n\n{self.name}\nID :{self.id}")
        elif len(info) == 1:
            self.name = info["name"]
            print(f"\n{self.name}")

i1 = student1(name="Imran",id = "1654",cg = 3.60)
i2 =  student1(name="Sayem",id = "1655")
i3 =  student1(name="Mohiuddin")


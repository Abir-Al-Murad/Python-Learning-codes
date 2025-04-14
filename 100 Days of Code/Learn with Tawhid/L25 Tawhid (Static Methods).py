# static method k call korar jonno class er proyojn hoy na ba static method class er upor kono effect dey na
# static method class er bahire rekheo kaj kora jay
# eta use kora hoy,,,jkhn amra chaibo j kono ekta method tarai use korte parbe jara spesifice kono class use korbe
#etate self argument dite hoy na
class Math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num + n
    @staticmethod
    def add(a,b):
        return a+b
result = Math.add(1,2)
print(result)
a= Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(7,2))
print(a.add(5,56))


print("****Learn With Tawhid****")

class student:
    uni_name = "BracU"
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print("Name:",self.name,"ID:",self.id,student.uni_name)
    @staticmethod
    def check_department(id):
        if id[3:5] == "01" :
            print("CSE")
        elif id[3:5] == "41" :
            print("CS")
student.check_department("14341007")    #static method call korar jonno object create kora lage na
s1 = student("Alur Vorta",520) #static method alada kore call korte hoy. jemon ekhane jodi
s2 = student("Kabir",420)      #kono student er department er dprtment check korte chai se
student.check_department("14301995")    #khetre alada kore static method call kore amra dept check
                                       #korte parbo
s1.details()
s2.details()



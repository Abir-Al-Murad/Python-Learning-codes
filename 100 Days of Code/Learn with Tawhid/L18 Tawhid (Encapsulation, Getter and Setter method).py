"""
get and set method use koreo amra private instance variable er access niye change
korte pari.
1st e set diye value change korbo(jehoto class er vitore private r public same)
2nd e get diye value return korbo.
"""
class Student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id #Private instance variable
    def details(self):
        print(f"Name:{self.name},ID:{self.__id}")
    def set_id(self,id):
        if(id>0):
            self.__id = id
        else:
            print("Invalid Id!!")
    def get_id(self):
        return self.__id
#===================================================================
s1 = Student("Sameer",112)
s2 = Student("Noman",111)
s3 = Student("Shohag",113)
s1.details()
s2.details()
s3.details()
s1.set_id(118)
s2.set_id(110)
s3.set_id(112)
print("New Id of s1:",s1.get_id())
print("New Id of s2:",s2.get_id())
print("New Id of s3:",s3.get_id())
print("       ID Number Updated       ")
s1.details()
s2.details()
s3.details()

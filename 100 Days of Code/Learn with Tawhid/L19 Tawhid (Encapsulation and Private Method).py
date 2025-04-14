class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id   #private instance variable
    def details(self):
        print(f"Name:{self.name},ID:{self.__id}")
        self.__method()
    def __method(self):  #private method
        print("Private method executed!!")
'''
private method class er bahire call kora jay na.

'''
#==========================================================
s1 = student("bob",11)
s2 = student("Labib",19)
#s1.__method()

s1.details()
s2.details()
class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id #Private instance variable
    def details(self):
        print("Name:",self.name,"ID:",self.__id)
    def update_Id(self,id): # private variable er access neyar jonno bikolpo system
        if(id>0):
            self.__id = id
        else:
            print("Invalid ID, Enter ID again.")
#Class er vitore private instance r public instance same
#==================================================================
s1 = student("Sakib",1010)
s2 = student("Kabir",1033)

s1.__id = 99 # private variable er access newoa jay na tai kaj korbe na
s1.update_Id(-9907) #invalid
s2.update_Id(1333) # kaj korbe + update korbe


s1.details()
s2.details()
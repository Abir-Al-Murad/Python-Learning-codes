class student:              #Grand parent class
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print("Name:",self.name,"ID:",self.id)
#==============================================
class csestudent(student):  #Parent Class
    def __init__(self,name,id,labs):
        super().__init__(name,id) #student class er init method theke name and id niye ashbe
        self.no_of_labs = labs
    def cry(self):
        print(self.name,"is crying because of",self.no_of_labs,"lab(s)")
#=======================================================================
class csefresher(csestudent):  #Child Class
    '''
    ekhane jehoto init method nai tai ei eta er parent class er init method use korbe.
    '''
    def enroll_cse110(self):
        print(self.name,"enrolled in cse110")
#==========================================================

s1 = csestudent("Azharul",1338,3)
s2 = csefresher("Anik",1337,1)
s1.details()
s2.cry()
s2.enroll_cse110()
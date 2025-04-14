#private variable er access shudu class er moddeh thakbe
class student:
    def __init__(self,name,id):
        self.name = name #Instance variable
        self.__id = id  #private instance variable (eta alada kore call+change kora jay na jemon s1.__id evabe
                        #tobe setter and getter system use kore call+change kora jay
    def details(self):
        print("Name:",self.name,"ID:",self.__id)

# eikhane __id eta private variable, shudu __id print korte chai..
#se khetre amaderk getter and setter method use korte hobe

    def set_ID(self,id): #setter diye information set korbo
        if (id>0):
            self.__id = id
        else:
            print("Invalid ID, enter ID again.")
    def get_id(self): #Getter diye information nibo ba get korbo #Getter always return korbe
        return self.__id

s1 = student("Abir",310)
s1.details()
s2 = student("Masud",311)
s1.set_ID(1302) #ager ta change kore new id set korlam
print(s1.get_id()) # change krito id alada kore print kora jay getter diye
s1.details()
s2.details()
s2.set_ID(1585) #ager ta change kore new id set korlam
s2.details()
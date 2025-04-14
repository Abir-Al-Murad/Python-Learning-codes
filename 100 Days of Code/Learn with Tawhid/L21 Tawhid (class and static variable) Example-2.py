'''
Amra jodi print korte chai j koyta student object creat hoice
'''
class student:
    count = 0 # eta class variable ba static variable
    def __init__(self,name,id):
        self.name = name
        self.id = id
        student.count +=1 #class call dile automatic INIT function call hobe tai count eijay increament kora hoyeche
        #and S1 koykbar call dileo init ekbar call hobe so count songkha sothik dekhabe
    def details(self):
        print(f"Name: {self.name},ID: {self.id},Student Count: {student.count}")

#=======================================================================================================================
print("Student Count:",student.count)
s1  = student("Ratul",248)
s2 = student("Labib",255)
s3 = student("Salauddin",534)
s3.details()
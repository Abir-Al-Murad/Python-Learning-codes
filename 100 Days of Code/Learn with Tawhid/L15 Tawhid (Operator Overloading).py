'''
                OPERATOR OVERLOADING(+)
--> To overload the (+) operator, we need to implement __add__() method in the class
'''
class data:
    def __init__(self,x):
        self.x = x
    #adding two objects
    def __add__(self, other):
        return self.x + other.x
#==========================================
num1 = data(10) #num1 is not an integer, it's a object of class
num2 = data(20)
str1 = data('CSE')
str2 = data('111')
print(num1+num2) #num1.__add__(num2)
print(str1+str2) #str1.__add__(str2)





#***********#**********#

'''
                    OPERATOR OVERLOADING(>)
--> To overload the(>) operator, we need to implement __get__() method in the class.
'''
class dat:
    def __init__(self,x):
        self.x = x
    def __gt__(self, other):
        if(self.x>other.x):
            return True
        else:
            return False
#=========================================
num3 = dat(10)
num4 = dat(20)
if(num3>num4):   #num3.__gt__(num4)
    print("Number 3 is greater than Number 4")
else:
    print("Number 4 is greater than Number 3")




#************#**************#
'''
                OPERATOR OVERLOADING(<)
--> To overload the (<) operator, we need to implement __lt__() method in the class
'''
class Data3:
    def __init__(self,x):
        self.x = x
    def __lt__(self, other):
        if(self.x < other.x):
            return "1st one is less than 2nd one"
        else:
            return "2nd one is less than 1st one"
#=====================================================
n = Data3(30)
n2 = Data3(20)
print(n<n2)     #n.__lt__(n2)





'''
                OPERATOR OVERLOADING(==)
To overload(==) operator, we need to implement __eq__() method in the class
'''
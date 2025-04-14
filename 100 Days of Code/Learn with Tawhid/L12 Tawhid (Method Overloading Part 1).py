        #Method 1
# class my_calculator:
#     def product(self,num1,num2):
#         print(num1*num2)
#     def product(self,num1,num2,num3):
#         print(num1*num2*num3)
# c1 = my_calculator()
# c1.product(4,5) #error ashbe  <<-----
# c1.product(6,9,8)
'''
same name er vinno parameter thakle take overloading bole
eikhane 1st product nam er method kaj korbe na 2nd ta kaj korbe
tai 8 number line e error ashbe
'''

        #Solution 1
'''
Evabe dile eikhetre 1,2,3 ta value porjonto neya jabe
'''
class my_calculator1():
    def product1(self,num1,num2=None,num3=None):
        if (num1 !=None and num2 !=None and num3 != None):
            print(num1*num2*num3)
        elif (num1 !=None and num2 !=None):
            print(num1*num2)
        else:
            print(1*num1)
#====================================================================

c2 = my_calculator1()
c2.product1(4,5)
c2.product1(4,5,6)



            #Solution 2
'''
Evabe joto iccha value neya jabe
'''
class my_calculator2:
    def product3(self,*nums):
        print(nums) # nums e joto value assign korbo sob tuple e porinoto hobe
        sum =1
        for i in nums:
            sum = sum * i
        print(sum)
#=================================================================================
c3 = my_calculator2()
c3.product3(4)
c3.product3(6,7)
c3.product3(9,6,7,1,5)
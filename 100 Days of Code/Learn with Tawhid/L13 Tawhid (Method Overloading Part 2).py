'''
Overloading --> Same name er method e different parameter thakle take overloading bole
dispatch use kore amra overloading korte pari
'''
from multipledispatch import dispatch
class my_calculator:
    @dispatch(int,int) #method 1
    def product(self,a,b):
        print(a*b)
    @dispatch(str,int,int) #method 2
    def product(self,a,b,c):
        print(int(a)*b*c)
    @dispatch(float,float,float) #method 3
    def product(self,a,b,c):
        print(a*b*c)
    @dispatch(str,str) #method 4
    def product(self,a,b):
        print(int(a)*int(b))
#=================================================================
c1 = my_calculator()
c1.product(4,5) #method 1 call hobe
c1.product("4",6,9) #method 2 call hobe
c1.product("6","9") #method 4 call hobe
c1.product(4.8,8.0,7.2) #method 3 call hobe
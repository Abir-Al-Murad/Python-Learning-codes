#Decorators function k Modify kore
def greet(fx): # greet nije ekta function nibe
    def mfx(*args,**kwargs): #*args arguments k tuple hisebe ney
        print("Good Morning") #**kwargs dictoranies hisebe ney(key,value)
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx
@greet # er mane greet name e function e hello function jabe and modify hobe
def hello():
    print("Hello World")
hello()
# @greet
def add(a,b):
    print(a+b)

# greet(hello)()    #@greet na diye eivabe o likha jay
greet(add)(1,2)
# add(1,2)

# Age thekei ekta function ache [hello()] but amra chacchi ei function age good morning and pore thanks janabe,,,sei khetre amra
# function k modify korte pari and setakei bole DECORATOR [greet()]
#DECORATOR baniye j j function upor apply korte chai sei function er age [@decorator_name] dite hbe





print("***Done By Myself***")
'''
def love():
    print("Love You Babe<3")
'''
#Eikhane amra chacchi j love you babe bolar age good morning bolbe
# Se khetre amra function k modify korte pari DECORATOR dara
def wish(func):
    def modified_function():
        print("Good Morning")
        func()
        print("Ghum Theke uthso?")
    return modified_function()
@wish #er mane love() func k wish() decorator er moddeh input kore dewoa
def love():
    print("Love You Babe<3")
love()



#Nicher code e ektu jhamela ache

print("**DONE BY AI**")

def decorator1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decorator2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decorator1
@decorator2
def my_function():
    return 10

print(my_function())  # Output: 400

'''
In this code, decorator1 and decorator2 are two decorators that modify the behavior of the original function
my_function. decorator1 squares the output of my_function, while decorator2 doubles it.
The @ symbol is used to chain the decorators together, with decorator1 being applied first, followed by decorator2.
When my_function is called, it executes the functionality added by both decorators, resulting in an output of 400.
'''
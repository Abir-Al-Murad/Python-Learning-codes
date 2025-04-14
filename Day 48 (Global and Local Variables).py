x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function





z=15
print(f"Value of Global Variable  z is:{z}")
def zoo():
    z=10 #Local variable
    print(f"Value of Local variable z is: {z}") #local variable works only in function

zoo()
print(f"This is Global variable cause it's out of function:{z}")

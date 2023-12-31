#The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.


x = [1,2,3,"Abir"]
print(dir(x))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__) #__dict__ variable k dictionary te convert kore

#The help() function is used to get help documentation for an object, including a description of its attributes and methods
print(help(Person))
print(help(str))
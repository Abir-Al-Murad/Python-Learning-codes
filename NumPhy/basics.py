import numpy as boss

#! This is a simple Array
array1 = boss.array([1,2,3],dtype='int')
print(array1)

#!Zeros (Matrix filled with Zeros)
print("\n\t\t----------Zeros----------")
zeros = boss.zeros((2,3),dtype='int')
print(zeros)

#!ones (Matrix filled with ones)
print("\n\t\t----------Ones------------")
ones = boss.ones((3,3),dtype="float")
print(ones)

#!Full (Matrix filled with a specific number)
print("\n\t\t----------Full------------")
full = boss.full((3,2),16) #(shape,number)
print(full)

#!Indetity
print("\n\t\t---------Identity----------")
idntty = boss.identity(5,dtype='int')
print(idntty)

#!Eye(Matrix with diagonal ones at an offset)
print("\n\t\t----------Eye------------")
eye = boss.eye(3,3,-1,dtype='int') #chage third parameter to see how it works
print(eye)

#!Arange(An array with a range and step size)
print("\n\t\t----------Arange------------")
arange = boss.arange(1,50,3) #(start,stop,step)
print(arange)

#!Linspace(An array with evenly spaced numbers)
print("\n\t\t---------LineSpace-----------")
linspace = boss.linspace(1,100,20,dtype='int') #(start,end,size)
print(linspace)
print("Size : ",linspace.size)

#!Empty(Empty matrix(Random Values))
print("\n\t\t----------Empty------------")
empty = boss.empty((3,5),dtype='int')
print(empty)
for i in range(5):
    empty[:,i] = i
print(empty)
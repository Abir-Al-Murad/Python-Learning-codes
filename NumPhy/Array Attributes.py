import numpy as np

a = np.array([1,2,3]) #One Dimentional Array or Vector
print(a)
print("Type of variable a is : ",type(a))
print("Shape of a variable : ",a.shape)
print("Dimention of a : ",a.ndim) #Dimention print korbe
print("DataType :",a.dtype)
print("Elements : ",a.size)
print("Memory Consumed : ",a.nbytes)

b = np.array([[1,2,3],
              [4,5,6]])
print(type(b),"\n",b.shape)
print("Dimention: ",b.ndim)


print("-----This is all About C Variable------")
c = np.array([[[1.77,2,3],
               [4,5,6],
               [8,7,9]]])
print(c)
print(c.shape)
print(c.dtype)
print("Total Elements in C variable: ",c.size)
print("Memory Consumed by C : ",c.nbytes)



d = np.array([ [[1,2,3],
               [4,5,6],
               [7,8,9]],
              
              [[10,11,12],
                [13,14,15],
                [16,17,18]]
                ])
print(d.shape)
print(d.dtype)

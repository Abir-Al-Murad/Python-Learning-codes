import numpy as np

#----indexing-----
arr1 = np.array([1,2,5,89,4])
print(arr1[0])
print(arr1[-1]) #arr1[len(arr1) - 1]

arr2 = np.random.randint(1,10,size=(3,3))
print(arr2)
print(arr2[1][1]) # Or arr2[1,1]

arr3 = np.random.randint(10,20,size=(2,3,3))
print(arr3)
print(arr3[1][2][2])

#!---------Slicing---------

print(arr1[0:3]) #Last index ta 1ta beshi dite hoy
print('Main Array2\n',arr2)
print('Sliced Array2\n',arr2[0:2,1:3]) # 0 theke 1 row er 1 to 2 index porjonto 
print("Sliced only one row ",arr2[0,1:3])
 
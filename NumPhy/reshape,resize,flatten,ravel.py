import numpy as np

'''
reshape() -> Doesn't modify Originals
resize() -> Modify Originals
flatten() -> Convert Arrays into 1D array. Doesn't Modify Originals
ravel() -> Convert Arrays into 1D array. Modify Originals
defining array shape
'''
#!-------Reshape--------
print("\n\t\t---------Resize(works with copy,doesn't change the main array)-----------")
a1 = np.array([[1,2,3],[4,5,6]])
print(a1.shape)
print("Main Array : \n",a1)
a_reshaped = a1.reshape((3,2)) 
print("Reshaped Array(Doesn't change the main array) : \n",a_reshaped)
# a_reshaped = a1.reshape((3,3)) #! This will thourgh error cs a1 have 6 element but reshaped array needs 9 elements

#!------Resize--------
print("\n\t\t---------Resize(works with reference,change the main array)-----------")
a1_resized = a1.resize((3,2)) # This will change the size of main a1 array
print('After resizing the a1 Array, The Main Array Changed: \n',a1)
a1_resized = np.resize(a1,(3,3)) # value ache 6 ta but eikhane lagbe 9 ta, eikhetre resize e value repeat hobe
print("Value Repeated : \n",a1_resized)



#!-------Ravel-----------
print("\n\t\t---------Ravel(Works With reference,Array k 1D array te convert kore)-----------")
a2 = np.random.randint(20,59,(2,3))
print('Main a2 Array :\n',a2)
a2_raveled = a2.ravel()
print("Raveled Array : ",a2_raveled)
a2_raveled[0] = 100
print("After changing the a2_raveled array , The Main Array(changed) : \n",a2)

#!-------flatten--------
print("\n\t\t---------Ravel(Works With Copy,Array k 1D array te convert kore)-----------")
a2_flatten = a2.flatten()
print("Flatten Array :",a2_flatten)
a2_flatten[1] = 2000 # This will not effect the main a2 array
print("After changing the a2_flatten array , The Main Array(not changed) : \n",a2)

#!--------Defining an array shape----------
print("\n\t\t---------Defining an Array Shape-----------")
b = np.array([[0,9,87],[48,74,5]])
print('Before change the shape of b: \n',b)
b.shape=(3,2)
print("After change the shape of b:\n",b)


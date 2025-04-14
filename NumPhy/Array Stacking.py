import numpy as np


a = np.array([1,2,4,52,3,5])
b = np.array([5,3,23,32,8,9])

print("Joining Vertically : \n",np.vstack((a,b))) #!vertically join korbe
print("Joining Horizontally : \n",np.hstack((a,b))) #!Horizontally join korbe
print("Column Stack : \n",np.column_stack((a,b))) #!Horizontally join korbe
print("Concatenate\n",np.concatenate((a,b),axis=0)) #! Merges two arrays along the specified axis
print('Depth Stack\n',np.dstack((a,b))) #! (Each pair of values is wrapped in a 3D format.)
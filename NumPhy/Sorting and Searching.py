import numpy as np

a = np.array([1,2,5,6,7,3,74,8,5,9,54,62,41,6,55])
print(np.sort(a))
print(np.argsort(a)) #!Returns indices of sorted elements
print("Index of max value : ",np.argmax(a)) #! Index of max value
print("Index of min value : ",np.argmin(a)) #! Index of min value
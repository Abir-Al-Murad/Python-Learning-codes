import numpy as np

arr1 = np.random.randint(10,20,(3,3))
arr2 = np.random.randint(30,40,(3,3))
print(f"Array1 : \n{arr1}\nArray2 : \n{arr2}")
print("Add : \n",np.add(arr1,arr2))
print("Subtract : \n",np.subtract(arr1,arr2))
print("Multiply : \n",np.multiply(arr1,arr2))
print("Divide : \n",np.divide(arr1,arr2))
print("Power : \n",np.power(arr1,2))
print("Square Root : \n",np.sqrt(arr1))

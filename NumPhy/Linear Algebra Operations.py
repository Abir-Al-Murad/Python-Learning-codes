import numpy as np

a = np.array([[1,2],[5,6]])
b = np.array([[5,6],[10,11]])
c = np.array([[12,14,13],[43,23,11],[12,23,32]])
print("Dot Product of Two Arrays : ",np.dot(a,b))
print("Matrix Mutiplication : ",np.matmul(a,b))
print("Matrix Mutiplication (Shortcut) : ",a @ b)
print("Inverse of a Matrix : ",np.linalg.inv(c))

'''
#! Determinant
 The determinant of a matrix gives information about the scaling factor and whether the matrix is invertible.
 If det = 0 → Matrix has no inverse.
'''
print("Determin of a Matrix : ",np.linalg.det(c))
print("Eigenvalues and Eigenvectors : ",np.linalg.eig(c))
'''
#! Eigenvalues and Eigenvectors
    λ (Eigenvalue) → Scalar that describes the stretching/shrinking factor
    𝑣 (Eigenvector) → A vector that does not change direction
'''
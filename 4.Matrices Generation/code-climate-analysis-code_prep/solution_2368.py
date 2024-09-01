# Importing library
import numpy as np

# Creating two 2X2 matrix
matrix1 = np.array([[1, 2], [0, 2]])
matrix2 = np.array([[0, 1], [3, 4]])

print("Original matrix:")
print(matrix1)
print(matrix2)

# Output
result = np.einsum("mk,kn", matrix1, matrix2)

print("Einsteins summation convention of the two matrix:")
print(result)
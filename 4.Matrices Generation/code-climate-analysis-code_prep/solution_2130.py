# Importing library
import numpy as np

# Creating a 2X2 matrix
matrix = np.array([[4, 2], [3, 1]])

print("Original matrix:")
print(matrix)

# Output
result = np.linalg.cond(matrix)

print("Condition number of the matrix:")
print(result)
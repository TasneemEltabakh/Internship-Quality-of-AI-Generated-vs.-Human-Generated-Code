# Importing library
import numpy as np

# Creating two 1-D arrays
array1 = np.array([6,2])
array2 = np.array([2,5])
print("Original 1-D arrays:")
print(array1)
print(array2)

# Output
print("Outer Product of the two array is:")
result = np.outer(array1, array2)
print(result)
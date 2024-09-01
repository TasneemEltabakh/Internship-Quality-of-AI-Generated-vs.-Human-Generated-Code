# importing Numpy package
import numpy as np

# creating a 1-D Numpy array
n_array = np.array([1, 0, 2, 0, 3, 0, 0, 5,
6, 7, 5, 0, 8])

print("Original array:")
print(n_array)

# finding indices of null elements using np.where()
print("\nIndices of elements equal to zero of the \
given 1-D array:")

res = np.where(n_array == 0)[0]
print(res)
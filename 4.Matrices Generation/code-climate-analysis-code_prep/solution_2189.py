# Python code to demonstrate
# flattening a 2d numpy array
# into 1d array

import numpy as np

ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# printing initial arrays
print("initial array", str(ini_array1))

# Multiplying arrays
result = ini_array1.flatten()

# printing result
print("New resulting array: ", result)
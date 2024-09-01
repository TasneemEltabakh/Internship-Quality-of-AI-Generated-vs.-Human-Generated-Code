# Python code to demonstrate
# multiplication of 2d array
# with 1d array

import numpy as np

ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
ini_array2 = np.array([0, 2, 3])

# printing initial arrays
print("initial array", str(ini_array1))

# Multiplying arrays
result = ini_array1 * ini_array2[:, np.newaxis]

# printing result
print("New resulting array: ", result)
# Python code to demonstrate
# to replace negative value with 0
import numpy as np

ini_array1 = np.array([1, 2, -3, 4, -5, -6])

# printing initial arrays
print("initial array", ini_array1)

# code to replace all negative value with 0
ini_array1[ini_array1<0] = 0

# printing result
print("New resulting array: ", ini_array1)
# Python code to demonstrate
# how to reverse numpy array
# using shortcut method

import numpy as np

# initialising numpy array
ini_array = np.array([1, 2, 3, 6, 4, 5])

# printing initial ini_array
print("initial array", str(ini_array))

# printing type of ini_array
print("type of ini_array", type(ini_array))

# using shortcut method to reverse
res = ini_array[::-1]

# printing result
print("final array", str(res))
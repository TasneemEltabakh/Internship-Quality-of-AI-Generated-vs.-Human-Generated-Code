# Python code to demonstrate converting
# array of strings to array of floats
# using astype


import numpy as np


# initialising array
ini_array = np.array(["1.1", "1.5", "2.7", "8.9"])


# printing initial array
print ("initial array", str(ini_array))


# converting to array of floats
# using np.astype
res = ini_array.astype(np.float)


# printing final result
print ("final array", str(res))
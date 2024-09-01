import numpy as np


# Original Array
array = np.array(['PHP C# Python C Java C++'], dtype=np.str)
print(array)

# Split the element of the said array with spaces
sparr = np.char.split(array)
print(sparr)
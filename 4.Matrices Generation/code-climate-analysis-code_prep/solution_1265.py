import numpy as np
array1 = [0, 1, 6, 1, 4, 1, 2, 2, 7] 
print("Original array:")
print(array1)
print("Number of occurrences of each value in array: ")
print(np.bincount(array1))

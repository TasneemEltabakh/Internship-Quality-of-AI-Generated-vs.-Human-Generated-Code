import numpy as np    
print("\nOriginal arrays:")
x = np.array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])
print(x)
print("\nNumber of dimensions:")
print(x.ndim)
print("Number of elements:")
print(x.size)
print("Number of bytes for each element in the said array:")
print(x.itemsize) 

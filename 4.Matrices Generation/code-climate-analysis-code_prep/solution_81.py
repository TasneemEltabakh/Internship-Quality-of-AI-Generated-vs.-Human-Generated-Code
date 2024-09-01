import numpy as np    
print("\nOriginal arrays:")
x = np.arange(16.0).reshape(4, 4)
print(x)
new_array1 =  np.vsplit(x, 2)
print("\nSplit an array into multiple sub-arrays vertically:")
print(new_array1)

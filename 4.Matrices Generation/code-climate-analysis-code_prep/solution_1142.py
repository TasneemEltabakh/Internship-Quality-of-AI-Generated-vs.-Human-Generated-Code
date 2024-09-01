import numpy as np    
print("\nOriginal arrays:")
x = np.arange(16.0).reshape(2, 2, 4)
print(x)
new_array1 = np.dsplit(x, 2)
print("\nsplit array into multiple sub-arrays along the 3rd axis:")
print(new_array1)

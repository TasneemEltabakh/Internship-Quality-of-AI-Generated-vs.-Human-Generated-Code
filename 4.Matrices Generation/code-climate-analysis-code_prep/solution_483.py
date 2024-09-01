import numpy as np
array_nums = np.arange(20).reshape(4,5)
print("Original array:")
print(array_nums)
print("\nAfter swapping column1 with column4:")
array_nums[:,[0,3]] = array_nums[:,[3,0]]
print(array_nums)

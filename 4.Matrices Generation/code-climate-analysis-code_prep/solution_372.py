import numpy as np
array_nums = np.arange(20).reshape(4,5)
print("Original array:")
print(array_nums)
print("\nAfter reversing:")
array_nums[:] = array_nums[3::-1]
print(array_nums)

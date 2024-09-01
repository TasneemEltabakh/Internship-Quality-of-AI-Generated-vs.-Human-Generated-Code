import numpy as np
nums = np.array([10, 20, 20, 20, 20, 0, 20, 30, 30, 30, 0, 0, 20, 20, 0])
print("Original array:")
print(nums)
print(np.count_nonzero(nums == 10))
print(np.count_nonzero(nums == 20))
print(np.count_nonzero(nums == 30))
print(np.count_nonzero(nums == 0))

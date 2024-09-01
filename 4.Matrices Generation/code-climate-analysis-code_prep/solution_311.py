import numpy as np
nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4))

import numpy as np
nums =  np.random.rand(10)
print("Original array:")
print(nums)
print("\nSorted first 5 elements:")
print(nums[np.argpartition(nums,range(5))])

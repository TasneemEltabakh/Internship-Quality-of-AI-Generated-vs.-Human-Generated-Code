import numpy as np
print("Original array:\n")
nums = np.random.randint(0,10,(3,3))
print(nums)
print("\nSort the said array by the nth column: ")
print(nums[nums[:,1].argsort()])

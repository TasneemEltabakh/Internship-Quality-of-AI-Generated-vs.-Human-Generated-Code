import numpy as np 
nums = np.random.randn(10, 4)
print("Original arrays:")
print(nums)
print("Set the array values with specified precision:")
np.set_printoptions(precision=4)
print(nums)

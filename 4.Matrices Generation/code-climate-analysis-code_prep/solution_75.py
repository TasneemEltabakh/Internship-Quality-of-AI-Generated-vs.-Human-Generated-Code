import numpy as np
print("Original array:")
nums = np.random.randint(0,3,(4,10))
print(nums)
print("\nTest whether the said array has null columns or not:")
print((~nums.any(axis=0)).any())

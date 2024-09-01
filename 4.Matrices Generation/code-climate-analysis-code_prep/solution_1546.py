import numpy as np
nums = np.array([1.2e-7, 1.5e-6, 1.7e-5])
print("Original arrays:")
print(nums)
print("Set the precision value to 10:")
np.set_printoptions(suppress=True, precision=10)
print(nums)

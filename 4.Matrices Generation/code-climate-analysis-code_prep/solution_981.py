import numpy as np 
nums = np.random.randint(10, size=(90, 30))
print("Original array:")
print(nums)
print("\nIncrease the number of items (10 edge elements) shown by the print statement:")
np.set_printoptions(edgeitems=10)
print(nums)

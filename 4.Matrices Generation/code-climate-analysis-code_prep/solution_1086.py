import numpy as np   
np.random.seed(32) 
nums = np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
print(nums)

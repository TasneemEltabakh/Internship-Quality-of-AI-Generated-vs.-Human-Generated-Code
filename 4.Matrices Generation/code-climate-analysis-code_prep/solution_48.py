import numpy as np
def generate():
   for n in range(15):
       yield n
nums = np.fromiter(generate(),dtype=float,count=-1)
print("New array:")
print(nums)

import numpy as np 

nums = np.array(['1.12', '2.23', '3.71', '4.23', '5.11'], dtype=np.str)
print("Original array:")
print(nums)
print("\nAdd two zeros to the beginning of each element of the said array:")
print(np.char.add('00', nums))
print("\nAlternate method:")
print(np.char.rjust(nums, 6, fillchar='0'))

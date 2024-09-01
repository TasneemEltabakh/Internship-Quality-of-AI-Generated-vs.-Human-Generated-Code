import numpy as np 
nums1 = np.array([[4.5, 3.5],
                 [5.1, 2.3]])
nums2 = np.array([[1],
                  [2]])
print("Original arrays:")
print(nums1)
print(nums2)
print("\nConcatenating the said two arrays:")
print(np.concatenate((nums1, nums2), axis=1))

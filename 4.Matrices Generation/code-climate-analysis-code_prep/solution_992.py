def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
nums1 = [10, 50, 40]
nums2 = [2, 5, 3]
print("Original list elements:")
print(nums1) 
print(nums2)
print("\nWeighted average of the said two list of numbers:")
print(weighted_average(nums1, nums2))
nums1 = [82, 90, 76, 83]
nums2 = [.2, .35, .45, 32]
print("\nOriginal list elements:")
print(nums1) 
print(nums2)
print("\nWeighted average of the said two list of numbers:")
print(weighted_average(nums1, nums2))

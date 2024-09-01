from heapq import merge
nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [0, 2, 4, 6, 8, 10]
print("Original sorted lists:")
print(nums1)
print(nums2)
print("\nAfter merging the said two sorted lists:")
print(list(merge(nums1, nums2)))

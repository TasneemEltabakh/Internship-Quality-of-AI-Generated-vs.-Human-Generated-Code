def matched_index(l1, l2):
    l2 = set(l2)
    return [i for i, el in enumerate(l1) if el in l2]

nums1 = [1, 2, 3, 4, 5 ,6]
nums2 = [7, 8, 5, 2, 10, 12]
print("Original lists:")
print(nums1)
print(nums2)
print("Compare said two lists and get the indices of the values present in both lists:")
print(matched_index(nums1, nums2))

nums1 = [1, 2, 3, 4, 5 ,6]
nums2 = [7, 8, 5, 7, 10, 12]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("Compare said two lists and get the indices of the values present in both lists:")
print(matched_index(nums1, nums2))

nums1 = [1, 2, 3, 4, 15 ,6]
nums2 = [7, 8, 5, 7, 10, 12]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("Compare said two lists and get the indices of the values present in both lists:")
print(matched_index(nums1, nums2))

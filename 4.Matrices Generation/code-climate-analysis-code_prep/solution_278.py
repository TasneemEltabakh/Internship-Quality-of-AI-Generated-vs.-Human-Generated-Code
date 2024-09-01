def drop_left_right(a, n = 1):
  return a[n:], a[:-n] 
nums = [1, 2, 3]
print("Original list elements:")
print(nums)
result = drop_left_right(nums)
print("Remove 1 element from left of the said list:")
print(result[0])
print("Remove 1 element from right of the said list:")
print(result[1])
nums = [1, 2, 3, 4]
print("\nOriginal list elements:")
print(nums)
result = drop_left_right(nums,2)
print("Remove 2 elements from left of the said list:")
print(result[0])
print("Remove 2 elements from right of the said list:")
print(result[1])
nums = [1, 2, 3, 4, 5, 6]
print("\nOriginal list elements:")
print(nums)
result = drop_left_right(nums)
print("Remove 7 elements from left of the said list:")
print(result[0])
print("Remove 7 elements from right of the said list:")
print(result[1])

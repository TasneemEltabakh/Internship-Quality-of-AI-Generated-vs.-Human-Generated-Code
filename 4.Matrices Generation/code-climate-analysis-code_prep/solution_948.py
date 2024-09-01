def min_n_nums(nums, n = 1):
  return sorted(nums, reverse = False)[:n]

nums = [1, 2, 3]
print("Original list elements:")
print(nums)
print("Minimum values of the said list:", min_n_nums(nums))
nums = [1, 2, 3]
print("\nOriginal list elements:")
print(nums)
print("Two minimum values of the said list:", min_n_nums(nums,2))
nums = [-2, -3, -1, -2, -4, 0, -5]
print("\nOriginal list elements:")
print(nums)
print("Threee minimum values of the said list:", min_n_nums(nums,3))
nums = [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
print("\nOriginal list elements:")
print(nums)
print("Two minimum values of the said list:", min_n_nums(nums, 2))

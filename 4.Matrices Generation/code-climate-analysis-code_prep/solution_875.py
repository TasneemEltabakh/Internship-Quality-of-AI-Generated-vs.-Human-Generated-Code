def max_n_nums(nums, n = 1):
  return sorted(nums, reverse = True)[:n]
nums = [1, 2, 3]
print("Original list elements:")
print(nums)
print("Maximum values of the said list:", max_n_nums(nums))
nums = [1, 2, 3]
print("\nOriginal list elements:")
print(nums)
print("Two maximum values of the said list:", max_n_nums(nums,2))
nums = [-2, -3, -1, -2, -4, 0, -5]
print("\nOriginal list elements:")
print(nums)
print("Threee maximum values of the said list:", max_n_nums(nums,3))
nums = [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
print("\nOriginal list elements:")
print(nums)
print("Two maximum values of the said list:", max_n_nums(nums, 2))

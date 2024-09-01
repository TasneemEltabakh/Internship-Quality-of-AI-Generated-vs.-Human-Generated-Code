nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Original list:")
print(nums)
nums[6:10], nums[1:3] = nums[1:3], nums[6:10]
print("\nSwap two sublists of the said list:")
print(nums)
nums[1:3], nums[4:6] = nums[4:6], nums[1:3]
print("\nSwap two sublists of the said list:")
print(nums)

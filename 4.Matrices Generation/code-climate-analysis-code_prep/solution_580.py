def move_end(nums, offset):
  return nums[offset:] + nums[:offset] 
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -3))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 8))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -8))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 7))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -7))

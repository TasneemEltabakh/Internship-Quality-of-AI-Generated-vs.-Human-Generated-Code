def every_nth(nums, nth):
  return nums[nth - 1::nth]
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))

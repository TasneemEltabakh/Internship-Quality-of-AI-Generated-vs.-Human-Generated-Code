def two_dimensional_list(nums):
  return list(zip(*nums))
print(two_dimensional_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
print(two_dimensional_list([[1, 2], [4, 5]]))

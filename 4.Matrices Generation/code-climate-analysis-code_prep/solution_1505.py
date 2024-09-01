def test_includes_all(nums, lsts):
  for x in lsts:
    if x not in nums:
      return False
  return True
print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 80]))

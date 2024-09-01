def find_index(nums, fn):
  return next(i for i, x in enumerate(nums) if fn(x))
print(find_index([1, 2, 3, 4], lambda n: n % 2 == 1))

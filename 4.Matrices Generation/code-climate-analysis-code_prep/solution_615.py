def is_contained_in(l1, l2):
  for x in set(l1):
    if l1.count(x) > l2.count(x):
      return False
  return True
print(is_contained_in([1, 2], [2, 4, 1]))
print(is_contained_in([1], [2, 4, 1]))
print(is_contained_in([1, 1], [4, 2, 1]))
print(is_contained_in([1, 1], [3, 2, 4, 1, 5, 1]))

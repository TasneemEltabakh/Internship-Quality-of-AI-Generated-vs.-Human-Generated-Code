def test(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)
print(test([1, 0, 2, 3], lambda x: x >= 3 ))
print(test([1, 0, 2, 3], lambda x: x < 0 ))
print(test([2, 2, 4, 4]))

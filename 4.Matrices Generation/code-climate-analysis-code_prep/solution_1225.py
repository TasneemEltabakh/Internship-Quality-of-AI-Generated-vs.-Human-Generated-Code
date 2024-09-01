def test(itr, fn):
  return dict(zip(itr, map(fn, itr)))
print(test([1, 2, 3, 4], lambda x: x * x))

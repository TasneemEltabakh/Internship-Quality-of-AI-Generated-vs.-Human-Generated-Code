def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
print(map_dictionary([1, 2, 3], lambda x: x * x))

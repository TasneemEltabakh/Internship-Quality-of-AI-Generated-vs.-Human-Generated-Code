def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
print(some([0, 1, 2, 0], lambda x: x >= 2 ))
print(some([5, 10, 20, 10], lambda x: x < 2 ))

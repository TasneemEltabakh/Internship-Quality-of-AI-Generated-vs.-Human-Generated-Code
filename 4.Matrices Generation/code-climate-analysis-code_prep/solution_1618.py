def every(lst, fn = lambda x: x):
  return all(map(fn, lst))
print(every([4, 2, 3], lambda x: x > 1))
print(every([4, 2, 3], lambda x: x < 1))
print(every([4, 2, 3], lambda x: x == 1))

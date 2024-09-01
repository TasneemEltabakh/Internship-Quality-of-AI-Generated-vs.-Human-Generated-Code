def symmetric_difference(x, y):
  (_x, _y) = (set(x), set(y))
  return [item for item in x if item not in _y] + [item for item in y
          if item not in _x]
print(symmetric_difference([10, 20, 30], [10, 20, 40]))

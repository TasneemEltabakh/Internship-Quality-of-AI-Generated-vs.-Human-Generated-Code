def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
print(bifurcate_by(['red', 'green', 'black', 'white'], lambda x: x[0] == 'w'))

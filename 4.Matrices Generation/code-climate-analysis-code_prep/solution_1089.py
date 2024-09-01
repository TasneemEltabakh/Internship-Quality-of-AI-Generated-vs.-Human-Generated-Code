def sum_by(lst, fn):
  return sum(map(fn, lst))
print(sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))

def union_by_el(x, y, fn):
  _x = set(map(fn, x))
  return list(set(x + [item for item in y if fn(item) not in _x])) 
from math import floor
print(union_by_el([4.1], [2.2, 4.3], floor))

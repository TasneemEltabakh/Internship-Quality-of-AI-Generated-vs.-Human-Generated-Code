from collections import defaultdict
def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
from math import floor
print(count_by([6.1, 4.2, 6.3], floor)) 
print(count_by(['one', 'two', 'three'], len))

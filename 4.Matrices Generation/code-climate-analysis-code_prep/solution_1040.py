from collections import defaultdict
def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq) 
print(frequencies(['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f'])) 
print(frequencies([3,4,7,5,9,3,4,5,0,3,2,3]))

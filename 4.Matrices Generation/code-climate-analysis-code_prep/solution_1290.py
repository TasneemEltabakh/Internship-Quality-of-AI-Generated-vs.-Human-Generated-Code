from math import floor, log
def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)] 
print(geometric_progression(256))
print(geometric_progression(256, 3))
print(geometric_progression(256, 1, 4))

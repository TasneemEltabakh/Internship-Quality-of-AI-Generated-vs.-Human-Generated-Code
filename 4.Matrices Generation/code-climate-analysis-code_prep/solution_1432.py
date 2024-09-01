def pluck(lst, key):
  return [x.get(key) for x in lst]
 
simpsons = [
  { 'name': 'Areeba', 'age': 8 },
  { 'name': 'Zachariah', 'age': 36 },
  { 'name': 'Caspar', 'age': 34 },
  { 'name': 'Presley', 'age': 10 }
]
print(pluck(simpsons, 'age'))

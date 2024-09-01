def test(d):
  return list(d.items())
 
d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
print("Original Dictionary:")
print(d)
print("\nConvert the said dictionary to a list of tuples:")
print(test(d))

def test(flat_dict):
  return list(flat_dict.values())
students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print("\nCreate a flat list of all the values of the said flat dictionary:")
print(test(students))

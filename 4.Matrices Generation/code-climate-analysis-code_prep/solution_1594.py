def keys_only(students):
  return list(students.keys()) 
students = {
  'Laura': 10,
  'Spencer': 11,
  'Bridget': 9,
  'Howard ': 10,
}
print("Original directory elements:")
print(students)
print("\nFlat list of all the keys of the said dictionary:")
print(keys_only(students))

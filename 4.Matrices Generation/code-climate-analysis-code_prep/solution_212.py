def test(lsts, key):
  return [x.get(key) for x in lsts]
 
students = [
  { 'name': 'Theodore', 'age': 18 },
  { 'name': 'Mathew', 'age': 22 },
  { 'name': 'Roxanne', 'age': 20 },
  { 'name': 'David', 'age': 18 }
]

print("Original list of dictionaries:")
print(students)
print("\nConvert a list of dictionaries into a list of values corresponding to the specified key:")
print(test(students, 'age'))

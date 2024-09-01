def test(students):
  return { value: key for key, value in students.items() }
 
students = {
  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,
}
print(test(students))

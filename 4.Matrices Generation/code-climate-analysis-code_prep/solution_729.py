from collections import defaultdict
def test(students):
  obj = defaultdict(list)
  for key, value in students.items():
    obj[value].append(key)
  return dict(obj)
 
students = {
  'Ora Mckinney': 8,
  'Theodore Hollandl': 7,
  'Mae Fleming': 7,
  'Mathew Gilbert': 8,
  'Ivan Little': 7,  
}
print(test(students))

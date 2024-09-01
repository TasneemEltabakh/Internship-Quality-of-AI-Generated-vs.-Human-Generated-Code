def test(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
 
users = {
  'Theodore': { 'user': 'Theodore', 'age': 45 },
  'Roxanne': { 'user': 'Roxanne', 'age': 15 },
  'Mathew': { 'user': 'Mathew', 'age': 21 },
}
print("\nOriginal dictionary elements:")
print(users)
print("\nDictionary with the same keys:")
print(test(users, lambda u : u['age']))

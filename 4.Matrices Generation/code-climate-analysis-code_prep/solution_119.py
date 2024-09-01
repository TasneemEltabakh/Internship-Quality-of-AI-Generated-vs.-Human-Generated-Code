from functools import reduce 
from operator import getitem
def get(d, selectors):
  return reduce(getitem, selectors, d) 
users = {
  'freddy': {
    'name': {
      'first': 'Fateh',
      'last': 'Harwood' 
    },
    'postIds': [1, 2, 3]
  }
}
print(get(users, ['freddy', 'name', 'last']))
print(get(users, ['freddy', 'postIds', 1]))

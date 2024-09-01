from functools import reduce 
from operator import getitem
def test(d, selectors):
  return reduce(getitem, selectors, d) 
users = {
  'Carla ': {
    'name': {
      'first': 'Carla ',
      'last': 'Russell' 
    },
    'postIds': [1, 2, 3, 4, 5]
  }
}
print(test(users, ['Carla ', 'name', 'last']))
print(test(users, ['Carla ', 'postIds', 1]))

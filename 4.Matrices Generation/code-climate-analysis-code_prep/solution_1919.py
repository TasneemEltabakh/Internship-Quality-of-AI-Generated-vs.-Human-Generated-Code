# importing the module
import json
from collections import namedtuple

# creating the data
data = '{"name" : "Geek", "id" : 1, "location" : "Mumbai"}'

# making the object
x = json.loads(data, object_hook =
lambda d : namedtuple('X', d.keys())
(*d.values()))

# accessing the JSON data as an object
print(x.name, x.id, x.location)
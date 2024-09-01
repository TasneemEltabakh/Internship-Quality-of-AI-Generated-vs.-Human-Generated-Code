import json


# create a sample json


a = {"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}


# Convert JSON to String


y = json.dumps(a)


print(y)
print(type(y))
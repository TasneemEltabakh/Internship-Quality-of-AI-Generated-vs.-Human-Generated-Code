# importing required librariess
import numpy as np
from ast import literal_eval

# creating class of string
name_list = """{
"column0": {"First_Name": "Akash",
"Second_Name": "kumar", "Interest": "Coding"},

"column1": {"First_Name": "Ayush",
"Second_Name": "Sharma", "Interest": "Cricket"},

"column2": {"First_Name": "Diksha",
"Second_Name": "Sharma","Interest": "Reading"},

"column3": {"First_Name":" Priyanka",
"Second_Name": "Kumari", "Interest": "Dancing"}

}"""
print("Type of name_list created:\n",
type(name_list))

# converting string type to dictionary
t = literal_eval(name_list)

# printing the original dictionary
print("\nPrinting the original Name_list dictionary:\n",
t)

print("Type of original dictionary:\n",
type(t))

# converting dictionary to numpy array
result_nparra = np.array([[v[j] for j in ['First_Name', 'Second_Name',
'Interest']] for k, v in t.items()])

print("\nConverted ndarray from the Original dictionary:\n",
result_nparra)

# printing the type of converted array
print("Type:\n", type(result_nparra))
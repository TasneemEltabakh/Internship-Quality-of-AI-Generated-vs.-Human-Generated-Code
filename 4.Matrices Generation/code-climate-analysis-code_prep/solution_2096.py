# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.


import pandas as pd


# initialise data of lists.
data = {'Category':['Array', 'Stack', 'Queue'],
'Marks':[20, 21, 19]}


# Create DataFrame
df = pd.DataFrame(data)


# Print the output.
print(df )
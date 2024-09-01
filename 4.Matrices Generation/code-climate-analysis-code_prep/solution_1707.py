# import modules
import pandas as pd

# create dataframe
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],
'Maths': [8, 5, 6, 9, 7],
'Science': [7, 9, 5, 4, 7],
'English': [7, 4, 7, 6, 8]}

df = pd.DataFrame(data)

# Sort the dataframes rows by Science,
# in descending order
a = df.sort_values(by ='Science', ascending = 0)
print("Sorting rows by Science:\n \n", a)
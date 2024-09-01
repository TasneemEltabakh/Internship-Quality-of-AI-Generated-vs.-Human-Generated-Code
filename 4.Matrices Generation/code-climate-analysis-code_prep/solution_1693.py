# Import pandas package
import pandas as pd

# create a dictionary with five fields each
data = {
'A':['A1', 'A2', 'A3', 'A4', 'A5'],
'B':['B1', 'B2', 'B3', 'B4', 'B4'],
'C':['C1', 'C2', 'C3', 'C3', 'C3'],
'D':['D1', 'D2', 'D2', 'D2', 'D2'],
'E':['E1', 'E1', 'E1', 'E1', 'E1'] }

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Get the unique values of 'B' column
df.B.unique()
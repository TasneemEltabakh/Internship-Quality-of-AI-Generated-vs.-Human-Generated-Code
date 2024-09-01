# importing pandas as pd
import pandas as pd

# sample dataframe
df = pd.DataFrame({
'A': [1, 2, 3, 4, 5],
'B': ['a', 'b', 'c', 'd', 'e'],
'C': [1.1, '1.0', '1.3', 2, 5] })

# converting all columns to string type
df = df.astype(str)
print(df.dtypes)
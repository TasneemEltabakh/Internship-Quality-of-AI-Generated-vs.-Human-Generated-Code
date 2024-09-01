import pandas as pd
df = pd.DataFrame({
    'id': [1, 1, 2, 3, 3, 4, 4, 4],
    'value': ['a', 'a', 'b', None, 'a', 'a', None, 'b']
})
print("Original DataFrame:")
print(df)
print("Count unique values:")
print (df.groupby('value')['id'].nunique())

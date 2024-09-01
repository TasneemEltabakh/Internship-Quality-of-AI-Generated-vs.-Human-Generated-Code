import pandas as pd
s = pd.date_range('2021-01-01', periods=12, freq='BM')
df = pd.DataFrame(s, columns=['Date'])
print('last working days of each month of a specific year:')
print(df)

import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nSighting days of the unidentified flying object (ufo) between 1949-10-10 and 1960-10-10:")
selected_period = df[(df['Date_time'] >= '1950-01-01 00:00:00') & (df['Date_time'] <= '1960-12-31 23:59:59')]
print(selected_period)

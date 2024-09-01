import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
now = pd.to_datetime('today')
print("Original Dataframe:")
print(df.head())
print("\nCurrent date:")
print(now)

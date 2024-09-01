import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
df['date_documented'] = df['date_documented'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nDifference (in days) between documented date and reporting date of UFO:")
df['Difference'] = (df['date_documented'] - df['Date_time']).dt.days
print(df)

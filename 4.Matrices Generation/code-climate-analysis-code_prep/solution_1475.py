import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nSighting years of the unidentified flying object:")
df["Year"] = df.Date_time.dt.year
print(df.head(10))

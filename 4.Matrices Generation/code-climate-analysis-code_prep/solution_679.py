import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nUnique reporting dates of UFO:")
print(df["Date_time"].map(lambda t: t.date()).unique())

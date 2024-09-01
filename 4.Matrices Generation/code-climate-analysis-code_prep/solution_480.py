import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
df['Year'] = df['Date_time'].apply(lambda x: "%d" % (x.year))
result = df.groupby(['Year', 'country']).size()
print("\nCountry-year wise frequency of reporting dates of UFO:")
print(result)

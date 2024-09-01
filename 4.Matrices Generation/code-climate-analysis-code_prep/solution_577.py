import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nPlot to present the number unidentified flying objects (ufo) found year wise:")
df["Year"] = df.Date_time.dt.year
df.Year.value_counts().sort_index().plot(x="Year")

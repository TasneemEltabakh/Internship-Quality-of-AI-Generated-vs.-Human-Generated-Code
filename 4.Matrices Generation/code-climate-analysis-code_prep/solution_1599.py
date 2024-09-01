import pandas as pd
#Source: https://bit.ly/1l9yjm9
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
most_sightings_years = df['Date_time'].dt.year.value_counts().head(10)
def is_top_years(year):
   if year in most_sightings_years.index:
       return year
hour_v_year = df.pivot_table(columns=df['Date_time'].dt.hour,index=df['Date_time'].dt.year.apply(is_top_years),aggfunc='count',values='city')
hour_v_year.columns = hour_v_year.columns.astype(int)
hour_v_year.columns = hour_v_year.columns.astype(str) + ":00"
hour_v_year.index = hour_v_year.index.astype(int)
print("\nComparison of the top 10 years in which the UFO was sighted vs the hours of the day:")
print(hour_v_year.head(10))

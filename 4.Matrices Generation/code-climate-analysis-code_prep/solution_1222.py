import pandas as pd
import datetime
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
now = pd.to_datetime('today')
duration = datetime.timedelta(days=365*40)
print("Original Dataframe:")
print(df.head())
print("\nCurrent date:")
print(now)
print("\nSighting days of the unidentified flying object (ufo) which are less than or equal to 40 years (365*40 days):")
df =  df[now - df['Date_time'] <= duration]
print(df.head())

import pandas as pd
from datetime import timedelta
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nAdd 100 days with reporting date:")
df['New_doc_dt'] = df['Date_time'] + timedelta(days=180)
print(df)

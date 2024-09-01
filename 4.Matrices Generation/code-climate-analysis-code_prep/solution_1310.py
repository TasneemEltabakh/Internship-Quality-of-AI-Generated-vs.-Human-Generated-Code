import pandas as pd
#Source: https://bit.ly/32kGinQ
df = pd.read_csv(r'ufo.csv')
df['date_documented'] = df['date_documented'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
# Add a new column instance, this adds a value to each instance of ufo sighting
df['instance'] = 1

# set index to time, this makes df a time series df and then you can apply pandas time series functions.
df.set_index(df['date_documented'], drop=True, inplace=True)

# create another df by resampling the original df and counting the instance column by Month ('M' is resample by month)
ufo2 = pd.DataFrame(df['instance'].resample('M').count())

# just to find month of resampled observation
ufo2['date_documented'] = pd.to_datetime(ufo2.index.values)

ufo2['month'] = ufo2['date_documented'].apply(lambda x: x.month)
print("Average mean of  the UFO (unidentified flying object) sighting was reported:")
print(ufo2.groupby(by='month').mean())

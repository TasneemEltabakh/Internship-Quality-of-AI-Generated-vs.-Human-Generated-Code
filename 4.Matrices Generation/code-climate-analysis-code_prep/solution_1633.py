import pandas as pd
import datetime as dt
import numpy as np
df = pd.DataFrame(index=pd.DatetimeIndex(start=dt.datetime(2019,1,1,0,0,1),
   end=dt.datetime(2019,1,1,10,0,1), freq='H'))\
   .reset_index().rename(columns={'index':'datetime'})
print("Sample datetime data:")
print(df.head(10))
df['ts'] = df.datetime.values.astype(np.int64) // 10 ** 9
print("\nConvert datetime to timestamp:")
print (df)

import pandas as pd
date_range = pd.timedelta_range(0, periods=49, freq='H')
print("Hourly range of perods 49:")
print(date_range)

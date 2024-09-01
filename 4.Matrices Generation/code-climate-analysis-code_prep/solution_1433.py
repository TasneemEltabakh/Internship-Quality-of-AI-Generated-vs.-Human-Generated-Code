import pandas as pd
result = pd.timedelta_range(0, periods=30, freq="1H20T")
print("For a frequency of 1 hours 20 minutes, here we have combined the hour (H) and minute (T):\n")
print(result)

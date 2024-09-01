import pandas as pd
dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
print("Month of December 2020:")
print(dates)
dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
print("\nMaximum date: ", dates.max())
print("Minimum date: ", dates.min())
print("Maximum index: ", dates.idxmax())
print("Minimum index: ", dates.idxmin())

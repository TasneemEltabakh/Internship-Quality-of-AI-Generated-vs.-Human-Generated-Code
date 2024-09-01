import pandas as pd
epoch_t = 1621132355
time_stamp = pd.to_datetime(epoch_t, unit='s')
# UTC (Coordinated Universal Time) is one of the well-known names of UTC+0 time zone which is 0h.
# By default, time series objects of pandas do not have an assigned time zone.
print("Regular time stamp in UTC:")
print(time_stamp)
print("\nConvert the said timestamp in to US/Pacific:")
print(time_stamp.tz_localize('UTC').tz_convert('US/Pacific'))
print("\nConvert the said timestamp in to Europe/Berlin:")
print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))

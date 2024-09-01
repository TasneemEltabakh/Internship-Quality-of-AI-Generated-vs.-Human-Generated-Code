import pandas as pd
dtt = pd.date_range('2018-01-01', periods=3, freq='H')
dtt = dtt.tz_localize('UTC')
print(dtt)
print("\nFrom UTC to America/Los_Angeles:")
dtt = dtt.tz_convert('America/Los_Angeles')
print(dtt)

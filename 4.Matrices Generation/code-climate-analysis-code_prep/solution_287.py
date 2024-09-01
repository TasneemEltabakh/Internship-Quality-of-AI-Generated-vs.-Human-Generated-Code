import pandas as pd
from pandas.tseries.holiday import *
sdt = datetime(2021, 1, 1)
edt = datetime(2030, 12, 31)
print("Holidays between 2021-01-01 and 2030-12-31 using the US federal holiday calendar.")
cal = USFederalHolidayCalendar()
for dt in cal.holidays(start=sdt, end=edt): 
    print (dt)

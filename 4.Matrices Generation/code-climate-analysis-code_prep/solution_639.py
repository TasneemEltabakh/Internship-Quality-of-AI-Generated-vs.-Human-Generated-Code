import pandas as pd
def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))
print("Check busines day or not?")
print('2020-12-01: ',is_business_day('2020-12-01'))
print('2020-12-06: ',is_business_day('2020-12-06'))
print('2020-12-07: ',is_business_day('2020-12-07'))
print('2020-12-08: ',is_business_day('2020-12-08'))

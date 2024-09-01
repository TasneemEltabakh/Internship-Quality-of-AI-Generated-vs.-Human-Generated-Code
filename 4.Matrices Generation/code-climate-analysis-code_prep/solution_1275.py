import pandas as pd
from datetime import date
now = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
print("Today's date:")
print(now)

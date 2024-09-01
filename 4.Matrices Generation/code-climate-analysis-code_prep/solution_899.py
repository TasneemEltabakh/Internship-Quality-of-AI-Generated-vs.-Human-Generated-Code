import pandas as pd
thursdays  = pd.date_range('2020-01-01', 
                           '2020-12-31', freq="W-THU")
print("All Thursdays between 2020-01-01 and 2020-12-31:\n")
print(thursdays.values)

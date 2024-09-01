import pandas as pd
time_series = pd.date_range('1/1/2021', periods = 36, freq='3M')
print("Time series using three months frequency:")
print(time_series) 

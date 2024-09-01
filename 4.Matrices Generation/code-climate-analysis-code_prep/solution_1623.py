import pandas as pd
import numpy as np
pi = pd.Series(np.random.randn(36), 
               pd.period_range('1/1/2029', 
                               '12/31/2031', freq='M'))
print("PeriodIndex which represents all the calendar month periods in 2029 and 2030:")
print(pi)
print("\nValues for all periods in 2030:")
print(pi['2030'])

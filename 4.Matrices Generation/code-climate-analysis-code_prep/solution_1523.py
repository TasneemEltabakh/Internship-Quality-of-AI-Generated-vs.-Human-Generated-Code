import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
result = df.sort_values('hire_date')
result

import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
result = df.set_index(['hire_date'])
result

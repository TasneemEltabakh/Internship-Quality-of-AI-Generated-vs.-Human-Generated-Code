import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df2 = df.set_index(['hire_date'])
result = df2["2005"]
result

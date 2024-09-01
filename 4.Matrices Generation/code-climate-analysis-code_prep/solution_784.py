import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
result = df.sort_values(by=['first_name','last_name'],ascending=[0,1])
result

import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
result = df[(df['hire_date'] >='Jan-2005') & (df['hire_date'] <= 'Dec-2006')].head()
result

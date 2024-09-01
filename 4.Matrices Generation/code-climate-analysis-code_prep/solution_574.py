import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')
df.insert(3, "column1", np.nan)
print(df.head) 

import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.loc[df['who']=='child'].isnull().sum()
print(result)

import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
print(result)

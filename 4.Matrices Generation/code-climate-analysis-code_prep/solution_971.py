import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived', index='sex', columns='class')
print(result)

import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table(index=['sex'], columns=['pclass'], aggfunc='count')
print(result)

import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
age = pd.cut(df['age'], [0, 10, 30, 60, 80])
result = df.pivot_table('survived', index=['sex',age], columns='pclass', aggfunc='count')
print(result)

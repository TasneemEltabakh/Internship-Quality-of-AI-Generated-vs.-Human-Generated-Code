import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = pd.cut(df['age'], [0, 10, 30, 60, 80])
print(result)

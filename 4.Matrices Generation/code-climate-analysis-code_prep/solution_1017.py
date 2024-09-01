import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table('sex',  'who', aggfunc = 'count')
print(result)

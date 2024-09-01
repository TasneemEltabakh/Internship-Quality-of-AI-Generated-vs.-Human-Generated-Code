import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived', ['sex' , 'alone' ], [ 'embark_town', 'class' ])
print(result)


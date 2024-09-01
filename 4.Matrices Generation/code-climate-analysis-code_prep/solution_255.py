import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = pd.pivot_table(df, index = ["sex","age"], aggfunc=np.sum)
print(result)

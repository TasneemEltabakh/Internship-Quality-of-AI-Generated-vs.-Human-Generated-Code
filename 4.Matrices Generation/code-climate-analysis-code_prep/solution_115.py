import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
print("List of columns:")
print(df.columns)
print("\nShape of the Dataset:")
print(df.shape)
print("\nData types of the Dataset:")
print(df.dtypes)

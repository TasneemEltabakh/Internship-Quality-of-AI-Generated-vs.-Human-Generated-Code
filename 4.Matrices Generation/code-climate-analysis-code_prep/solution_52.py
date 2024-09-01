import pandas as pd
df = pd.read_csv(r'ufo.csv')
print(df.isnull().sum())

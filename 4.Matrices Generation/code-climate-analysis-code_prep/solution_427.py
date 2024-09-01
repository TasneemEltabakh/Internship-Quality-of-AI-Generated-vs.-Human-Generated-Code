import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')
df_sub=df[["MSHA ID","Labor_Hours"]].groupby('MSHA ID').sum()
df_sub

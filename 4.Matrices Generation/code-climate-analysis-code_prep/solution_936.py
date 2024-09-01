import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')
sum_row=df[["Production", "Labor_Hours"]].sum()
df_sum=pd.DataFrame(data=sum_row).T
df_sum=df_sum.reindex(columns=df.columns)
df_sum

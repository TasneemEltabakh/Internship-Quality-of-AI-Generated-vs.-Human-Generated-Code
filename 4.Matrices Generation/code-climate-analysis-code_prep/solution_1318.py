import pandas as pd
import numpy as np
df = pd.read_excel('E:\SaleData.xlsx')
table = pd.pivot_table(df,index="Region",values="Sale_amt", aggfunc = np.sum)
print(table)

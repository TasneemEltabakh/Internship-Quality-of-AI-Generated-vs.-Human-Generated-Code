import pandas as pd
import numpy as np
df = pd.read_excel('E:\SaleData.xlsx')
print(pd.pivot_table(df,index=["Manager"],values=["Sale_amt"],aggfunc=[np.mean,len]))

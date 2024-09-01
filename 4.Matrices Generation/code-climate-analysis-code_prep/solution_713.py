import pandas as pd
import numpy as np
df = pd.read_excel('E:\SaleData.xlsx')
table = pd.pivot_table(df,index=["Manager","SalesMan"],values=["Units","Sale_amt"],
               aggfunc=[np.sum],fill_value=0,margins=True)
print(table)

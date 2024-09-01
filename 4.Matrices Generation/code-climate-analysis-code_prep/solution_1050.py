import pandas as pd
import numpy as np
df = pd.read_excel('E:\SaleData.xlsx')
print(pd.pivot_table(df,index=["Item"], values="Units", aggfunc=np.sum))

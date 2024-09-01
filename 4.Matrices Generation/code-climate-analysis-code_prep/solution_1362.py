import pandas as pd
df = pd.read_excel('E:\SaleData.xlsx')
print(df)
pd.pivot_table(df,index=["Region","SalesMan"])

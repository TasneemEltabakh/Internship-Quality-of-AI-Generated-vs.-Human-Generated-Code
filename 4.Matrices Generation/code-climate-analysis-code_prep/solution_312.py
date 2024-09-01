import pandas as pd
df = pd.read_excel('E:\SaleData.xlsx')
table = pd.pivot_table(df,index=["Region","Manager","SalesMan"], values="Sale_amt")
print(table.query('Manager == ["Douglas"]'))

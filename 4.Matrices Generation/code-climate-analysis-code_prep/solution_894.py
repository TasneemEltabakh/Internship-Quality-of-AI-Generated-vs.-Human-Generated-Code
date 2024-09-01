import pandas as pd
df = pd.read_excel('E:\SaleData.xlsx')
table = pd.pivot_table(df,index=["Region", "Item"], values="Units")
print(table.query('Item == ["Television","Home Theater"]'))

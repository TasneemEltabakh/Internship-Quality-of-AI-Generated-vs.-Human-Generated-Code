# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
'Product':['Umbrella', 'Matress', 'Badminton', 'Shuttle'],
'Last_Price':[1200, 1500, 1600, 352],
'Updated_Price':[1250, 1450, 1550, 400],
'Discount':[10, 10, 10, 10]})

# Create the indexes
df.index =['Item 1', 'Item 2', 'Item 3', 'Item 4']

# Print the dataframe
print(df)
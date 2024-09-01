# importing pandas as pd
import pandas as pd


# Creating the dataframe
df = pd.DataFrame({'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
'Event':['Music', 'Poetry', 'Theatre'],
'Cost':[10000, 5000, 15000]})


# Print the dataframe
print(df)


# Now we will check the data type
# of the 'Date' column
df.info()
# Import pandas library
import pandas as pd


# initialize list of lists
data = [['Geeks', 10], ['for', 15], ['geeks', 20]]


# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age'])


# print dataframe.
print(df )
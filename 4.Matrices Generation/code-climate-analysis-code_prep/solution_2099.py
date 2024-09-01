# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("diamonds.csv")

# sorting data frame by a column
data.sort_values("carat", axis=0, ascending=True,
inplace=True, na_position='first')

# display
data.head(10)
# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

ser = pd.Series(df['Name'])
ser.head(10)
# or simply df['Name'].head(10)
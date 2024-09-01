# import the required packages
import pandas as pd

# Define the dictionary for converting to dataframe
movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
'Year': ['1972', '2018', '1999'],
'Rating': ['9.2', '6.8', '8.8']}

df = pd.DataFrame(movies)
print(df)
# import Pandas as pd
import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior', 'Jonny Depp'],
'Age':[32, 34, 36]})

print("Given Dataframe is :\n",df)

# bydefault splitting is done on the basis of single space.
print("\nSplitting 'Name' column into two different columns :\n",
df.Name.str.split(expand=True))
import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFiltering records by label or index:")
print(w_a_con.loc[0:4, ["WHO region", "Beverage Types"]])

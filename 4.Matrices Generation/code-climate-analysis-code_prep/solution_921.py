import pandas as pd
# World alcohol consumption data
new_w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(new_w_a_con.head())
print("\nFilter by matching multiple values in a given dataframe:")
flt_wine = new_w_a_con["WHO region"].isin(["Africa", "Eastern Mediterranean", "Europe"])
print(new_w_a_con[flt_wine])

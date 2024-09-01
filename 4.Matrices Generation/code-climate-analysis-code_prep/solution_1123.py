import pandas as pd
# World alcohol consumption data
new_w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(new_w_a_con.head())
print("\nSelect all rows which not appears in a given list:")
who_region = ["Africa", "Eastern Mediterranean", "Europe"]
flt_wine = ~new_w_a_con["WHO region"].isin(who_region)
print(new_w_a_con[flt_wine])

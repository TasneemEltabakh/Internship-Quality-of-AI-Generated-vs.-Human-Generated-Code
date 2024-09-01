import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
# Remove NA / NaN values
new_w_a_con = w_a_con.dropna()
print("\nMatch if  a given column has a particular sub string:")
print(new_w_a_con[new_w_a_con["WHO region"].str.contains("Ea")])

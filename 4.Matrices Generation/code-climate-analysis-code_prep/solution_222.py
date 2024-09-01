import pandas as pd 

# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFind which years have all non-zero values:")
print(w_a_con.loc[:,w_a_con.all()])
print("\nFind which years have any non-zero values:")
print(w_a_con.loc[:,w_a_con.any()])

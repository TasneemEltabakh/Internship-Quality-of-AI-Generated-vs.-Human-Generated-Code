import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nMissing values:")
print(w_a_con.isnull())
print("\nDropping the missing values:")
print(w_a_con.dropna())

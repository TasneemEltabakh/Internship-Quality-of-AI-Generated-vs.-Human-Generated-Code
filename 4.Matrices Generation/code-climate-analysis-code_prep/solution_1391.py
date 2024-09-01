import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nSelect random number of rows:")
print(w_a_con.sample(5))
print("\nSelect fraction of randome rows:")
print(w_a_con.sample(frac=0.02))

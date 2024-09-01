import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nStarting from the 2nd row, access every 5th row:")
print(w_a_con.iloc[1::5].head(10))

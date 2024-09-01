import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFilter rows based on row numbers ended with 0, like 0, 10, 20, 30:")
print(w_a_con.filter(regex='0$', axis=0))

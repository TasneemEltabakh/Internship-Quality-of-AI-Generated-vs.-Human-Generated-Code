import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nThe world alcohol consumption details where year is 1987 or 1989:")
print((w_a_con[(w_a_con['Year']==1987) | (w_a_con['Year']==1989)]).head(10))

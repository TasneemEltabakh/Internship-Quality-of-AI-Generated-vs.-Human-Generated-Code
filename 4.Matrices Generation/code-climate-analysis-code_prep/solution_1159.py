import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFrom the 'Year' column, access every other column:")
print(w_a_con.loc[:,'Year'::2].head(10))
print("\nAlternate solution:")
print(w_a_con.iloc[:,0::2].head(10))

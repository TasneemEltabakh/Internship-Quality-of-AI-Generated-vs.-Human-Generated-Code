import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nSelect consecutive columns:")
print(w_a_con.loc[:,"Country":"Display Value"].head())
print("\nAlternate command:")
print(w_a_con.iloc[:,2:5].head())
print("\nSelect rows with Index label 0 to 9 with specific columns:")
print(w_a_con.loc[0:9,["Year","Country","Display Value"]])

import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nThe world alcohol consumption details: average consumption of \nbeverages per person >=5 and Beverage Types is Beer:")
print(w_a_con[(w_a_con['Display Value'] >= 5) & (w_a_con['Beverage Types'] == 'Beer')].head(10))

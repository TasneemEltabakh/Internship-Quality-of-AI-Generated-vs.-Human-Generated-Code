import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFilter all records where the average consumption of beverages per person from .5 to 2.50.:")
print(w_a_con[(w_a_con['Display Value'] < 2.5) & (w_a_con['Display Value']>.5)].head())

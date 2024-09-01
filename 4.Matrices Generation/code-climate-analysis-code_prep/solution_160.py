import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nAverage consumption of wine per person greater than 2:")
print(w_a_con[(w_a_con['Beverage Types'] == 'Wine') & (w_a_con['Display Value'] > .2)].count())

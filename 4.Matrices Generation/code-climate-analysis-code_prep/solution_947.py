import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
new_w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nRename all the column names:")
w_a_con.columns = ['year','who_region','country','beverage_types','display_values']
print(w_a_con.head())
print("\nRenaming only some of the column names:")
new_w_a_con.rename(columns = {"WHO region":"WHO_region","Display Value":"Display_Value" },inplace = True)
print(new_w_a_con.head()) 

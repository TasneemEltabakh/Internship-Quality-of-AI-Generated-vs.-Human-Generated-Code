import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nFind  all columns which all entries present:")
print(w_a_con.loc[:, w_a_con.notnull().all()])
print("\nRows and columns has a NaN:")
print(w_a_con.loc[:,w_a_con.isnull().any()])
print("\nDrop rows with any NaNs:")
print(w_a_con.dropna(how='any'))  

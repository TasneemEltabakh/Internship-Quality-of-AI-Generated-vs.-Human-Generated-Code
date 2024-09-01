import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nThe world alcohol consumption details in the year 1985:")
print(w_a_con[w_a_con['Year']==1985].head(10))
print("\nThe world alcohol consumption details in the year 1989:")
print(w_a_con[w_a_con['Year']==1989].head(10))

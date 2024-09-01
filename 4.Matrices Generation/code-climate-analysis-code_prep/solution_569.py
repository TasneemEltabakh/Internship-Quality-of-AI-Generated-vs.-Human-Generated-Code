import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nThe world alcohol consumption details in the year 1986 or 1989 where  WHO region is Americas  or 'Europe':")
print(w_a_con[((w_a_con['Year']==1985) | (w_a_con['Year']==1989)) & ((w_a_con['WHO region']=='Americas') | (w_a_con['WHO region']=='Europe'))].head(10))

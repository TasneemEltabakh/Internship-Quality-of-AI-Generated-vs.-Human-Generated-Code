import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nThe world alcohol consumption details in the year 1986 where WHO region is Western Pacific and country is VietNam :")
print(w_a_con[(w_a_con['Year']==1986) & (w_a_con['WHO region']=='Western Pacific') & (w_a_con['Country']=='Viet Nam')])

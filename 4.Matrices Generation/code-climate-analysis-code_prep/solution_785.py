import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32]})
     
print("Original DataFrame:")
print(df)
print("\nDefault Index Range:")
print(df.index)
df.index += 10 
print("\nNew Index Range:")
print(df.index)
print("\nDataFrame with new index:")
print(df)

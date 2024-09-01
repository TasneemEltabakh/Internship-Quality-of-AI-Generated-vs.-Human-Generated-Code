import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32],
    'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})    
print("Original DataFrame:")
print(df)
print("\nCreate MultiIndex on 'tcode' and 'school_code':")
df = df.set_index(['tcode', 'school_code'])
print(df)
print("\nSelect rows(s) from 'tcode' column:")
print(df.query("tcode == 't2'"))
print("\nSelect rows(s) from 'school_code' column:")
print(df.query("school_code == 's001'"))
print("\nSelect rows(s) from 'tcode' and 'scode' columns:")
print(df.query(("tcode == 't1'") and ("school_code == 's001'")))

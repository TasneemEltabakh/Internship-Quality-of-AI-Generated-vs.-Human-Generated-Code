import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.1111','920 N. Bishop Ave.','9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court']
    })
print("Original DataFrame:")
print(df)
def test_num_great(text): 
    result = re.findall(r'95[5-9]|9[6-9]\d|[1-9]\d{3,}',text)
    return " ".join(result)
df['num_great']=df['address'].apply(lambda x : test_num_great(x))
print("\nNumber greater than 940:")
print(df)

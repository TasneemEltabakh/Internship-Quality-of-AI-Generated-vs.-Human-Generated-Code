import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

def test_num_less(n):
    nums = []
    for i in n.split():
        result = re.findall(r'\b(0*(?:[1-9][0-9]?|100))\b',i)
        nums.append(result)
        all_num=[",".join(x) for x in nums if x != []]
    return " ".join(all_num)

df['num_less'] = df['address'].apply(lambda x : test_num_less(x))
print("\nNumber less than 100:")
print(df)

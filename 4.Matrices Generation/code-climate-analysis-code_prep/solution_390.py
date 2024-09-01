import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print("Original DataFrame:")
print(df)
def find_year(text):
    #line=re.findall(r"\b(18[0][0]|2[0-2][00])\b",text)
    result = re.findall(r"\b(18[0-9]{2}|19[0-8][0-9]|199[0-9]|2[01][0-9]{2}|2200)\b",text)
    return result
df['year_range']=df['year'].apply(lambda x: find_year(x))
print("\Extracting year between 1800 to 2200:")
print(df)

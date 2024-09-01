import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001.','c000,2','c0003', 'c0003#', 'c0004,'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print("Original DataFrame:")
print(df)
def find_punctuations(text):
    result = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string="".join(result)
    return list(string)
df['nonalpha']=df['company_code'].apply(lambda x: find_punctuations(x))
print("\nExtracting punctuation:")
print(df)

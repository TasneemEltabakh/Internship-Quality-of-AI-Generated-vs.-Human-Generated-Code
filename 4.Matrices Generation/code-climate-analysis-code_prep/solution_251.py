import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']
})

print("Original DataFrame:")
print(df)

def find_capital_word(str1):
    result = re.findall(r'\b[A-Z]\w+', str1)
    return result

df['caps_word_in']=df['address'].apply(lambda cw : find_capital_word(cw))
print("\nExtract words starting with capital words from the sentences':")
print(df)

import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue\n9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.\n102 Dunbar St.', '17 West Livingston Court']
})

print("Original DataFrame:")
print(df)

def find_unique_sentence(str1):
    result = re.findall(r'(?sm)(^[^\r\n]+$)(?!.*^\1$)', str1)
    return result

df['unique_sentence']=df['address'].apply(lambda st : find_unique_sentence(st))
print("\nExtract unique sentences :")
print(df)

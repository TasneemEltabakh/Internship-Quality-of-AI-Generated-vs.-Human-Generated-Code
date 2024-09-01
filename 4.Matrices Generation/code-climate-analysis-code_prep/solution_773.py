import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court']
})
print("Original DataFrame:")
print(df)
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result
df['with_out_tags']=df['address'].apply(lambda cw : remove_tags(cw))
print("\nSentences without tags':")
print(df)

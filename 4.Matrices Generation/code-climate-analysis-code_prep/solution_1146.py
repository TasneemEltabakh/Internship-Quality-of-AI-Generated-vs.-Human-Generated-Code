import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'text_code': ['t0001.','t0002','t0003', 't0004'],
    'text_lang': ['She livedd a long life.', 'How oold is your father?', 'What is tthe problem?','TThhis desk is used by Tom.']
    })
print("Original DataFrame:")
print(df)
def rep_char(str1):
    tchr = str1.group(0)
    if len(tchr) > 1:
        return tchr[0:1] # can change the value here on repetition
def unique_char(rep, sent_text):
    convert = re.sub(r'(\w)\1+', rep, sent_text) 
    return convert
df['normal_text']=df['text_lang'].apply(lambda x : unique_char(rep_char,x))
print("\nRemove repetitive characters:")
print(df)
